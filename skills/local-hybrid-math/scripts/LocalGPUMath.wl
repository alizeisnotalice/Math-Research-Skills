BeginPackage["LocalGPUMath`"];
MetalEvaluate::usage = "MetalEvaluate[op, x] evaluates SinExp or Fourier on native Apple GPUArray objects. Input must already be NumericArray[..., Real32], or explicitly allow precision loss.";
MetalEvaluate::precision = "Provide a Real32 NumericArray, or use \"AllowPrecisionLoss\"->True. Arbitrary precision and exact arithmetic stay on CPU.";
MetalEvaluate::gpu = "The operation did not keep GPUArray inputs and output; no GPU success is claimed.";
MetalEvaluate::operation = "Supported native Apple operations are SinExp and Fourier.";
MetalEvaluate::input = "Input must be a finite, nonempty real vector or matrix (Fourier: vector).";
Options[MetalEvaluate] = {"AllowPrecisionLoss" -> False};
Begin["`Private`"];
MetalEvaluate[op_String, x_, OptionsPattern[]] := Module[
  {host, source, gx, gy, y, reference, elapsed, error, relative, passed},
  If[!MemberQ[{"SinExp", "Fourier"}, op], Message[MetalEvaluate::operation]; Return[$Failed]];
  If[!(Head[x] === NumericArray && NumericArrayType[x] === "Real32") &&
     !TrueQ[OptionValue["AllowPrecisionLoss"]],
    Message[MetalEvaluate::precision]; Return[$Failed]];
  source = If[Head[x] === NumericArray, Normal[x], x];
  If[!(ArrayQ[source, _, (NumberQ[#] && Im[N[#]] == 0 && Abs[N[#]] < Infinity &)] &&
       1 <= ArrayDepth[source] <= 2 && Length[Flatten[source]] > 0) ||
     (op === "Fourier" && !VectorQ[source]), Message[MetalEvaluate::input]; Return[$Failed]];
  host = Quiet@Check[NumericArray[source, "Real32"], $Failed];
  If[host === $Failed, Message[MetalEvaluate::input]; Return[$Failed]];
  If[ByteCount[host] > 128*1024^2, Message[MetalEvaluate::input]; Return[$Failed]];
  gx = Quiet@Check[GPUArray[host], $Failed];
  If[!TrueQ[GPUArrayQ[gx]], Message[MetalEvaluate::gpu]; Return[$Failed]];
  {elapsed, y} = AbsoluteTiming[
    gy = If[op === "SinExp", Sin[gx] Exp[-gx^2], Fourier[gx]];
    If[!TrueQ[GPUArrayQ[gy]], Return[$Failed]];
    Normal[gy]
  ];
  If[y === $Failed, Message[MetalEvaluate::gpu]; Return[$Failed]];
  reference = If[op === "SinExp", Sin[Normal[host]] Exp[-Normal[host]^2], Fourier[Normal[host]]];
  error = Max[Abs[Flatten[y - reference]]];
  relative = Norm[Flatten[y - reference]]/Max[Norm[Flatten[reference]], 10.^-30];
  passed = TrueQ[Max[Abs[Flatten[y-reference]]/
      (5.*^-5 + 5.*^-4 Abs[Flatten[reference]])] <= 1];
  <|"ok" -> passed, "route" -> "native-wolfram-apple-gpuarray", "operation" -> op,
    "input_gpu" -> TrueQ[GPUArrayQ[gx]], "output_gpu" -> TrueQ[GPUArrayQ[gy]],
    "input_dtype" -> NumericArrayType[host], "output_dtype" -> gy["ElementType"],
    "compute_and_materialize_seconds" -> elapsed,
    "input_max_abs_rounding" -> Max[Abs[Flatten[N[source] - Normal[host]]]],
    "max_abs_error" -> error, "relative_l2_error" -> relative,
    "reference" -> "CPU machine arithmetic on the same Real32-rounded inputs",
    "evidence_class" -> "numerical-check-not-rigorous-proof", "result" -> y|>
];
End[];
EndPackage[];
