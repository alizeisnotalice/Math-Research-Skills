% Exact finite audit of formal-math eth/proof/statements/EightSquareStatement.lean.
% It implements Block, bxor, phi, sigma and Signs literally on all 3-bit blocks.
% Scope: Equation (12) / Signs only; it is not a check of Lemma 2 or an ETH proof.

blocks = dec2bin(0:7) - '0';  % rows are (p1,p2,p3), as in the Lean tuple order
settings = 0;
support = 0;
diagonal = 0;
cancellation = 0;
failures = 0;

for ip = 1:8
  p = blocks(ip,:);
  for iq = 1:8
    q = blocks(iq,:);
    for ir = 1:8
      r = blocks(ir,:);
      for is = 1:8
        s = blocks(is,:);
        settings = settings + 1;
        sameXor = all(xor(p,q) == xor(r,s));
        if sameXor
          support = support + 1;
        end
        lhs = 2 * all(p == r) * all(q == s);
        rhs = sameXor * (sigma(p,q) * sigma(r,s) + sigma(p,s) * sigma(r,q));
        if lhs ~= rhs
          failures = failures + 1;
        end
        if sameXor && all(q == s)
          diagonal = diagonal + 1;
        elseif sameXor
          cancellation = cancellation + 1;
          % This is precisely Eight.Signs with (p,q,p',q')=(p,q,r,s).
          if sigma(p,q) * sigma(r,s) + sigma(p,s) * sigma(r,q) ~= 0
            failures = failures + 1;
          end
        end
      end
    end
  end
end

fprintf('settings=%d support=%d diagonal=%d cancellation=%d failures=%d\n', ...
  settings, support, diagonal, cancellation, failures);
assert(settings == 4096 && support == 512 && diagonal == 64 && cancellation == 448);
assert(failures == 0);

function z = sigma(p,q)
  % Eight.phi, term for term, using exact integer arithmetic at this scale.
  phi = p(1)*q(1) + p(1)*q(2) + p(1)*q(3) + p(2)*q(2) + p(2)*q(3) + p(3)*q(3) ...
      + q(1)*p(2)*p(3) + p(1)*q(2)*p(3) + p(1)*p(2)*q(3);
  z = (-1)^phi;
end
