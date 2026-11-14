% Numerical consistency checks for identities stated in W23S006.
% This does not prove any SAW theorem; proof evidence is the read source.
format long g
mu_from_fugacity = 2*cos(pi/8);
mu_closed_form = sqrt(2 + sqrt(2));
paired_phase_sum = 2*cos(3*pi/2);
xc_from_source = 1/mu_from_fugacity;
xc_closed_form = 1/sqrt(2 + sqrt(2));
fprintf('2*cos(pi/8)          = %.16g\n', mu_from_fugacity);
fprintf('sqrt(2+sqrt(2))       = %.16g\n', mu_closed_form);
fprintf('connective residual   = %.3g\n', mu_from_fugacity-mu_closed_form);
fprintf('paired phase sum      = %.3g\n', paired_phase_sum);
fprintf('critical fugacity     = %.16g\n', xc_from_source);
fprintf('closed-form xc        = %.16g\n', xc_closed_form);
fprintf('fugacity residual     = %.3g\n', xc_from_source-xc_closed_form);
fprintf('Hammersley-Welsh B threshold pi*sqrt(2/3) = %.16g\n', pi*sqrt(2/3));
