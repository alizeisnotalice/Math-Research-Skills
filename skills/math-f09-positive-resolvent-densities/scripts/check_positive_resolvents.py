#!/usr/bin/env python3
"""Finite numerical replay for the two local positive-resolvent identities."""

import numpy as np


def normalized_circle_integral(values):
    return sum(values) / len(values)


def main():
    sample_count = 4096
    circle = np.exp(2j * np.pi * np.arange(sample_count) / sample_count)
    identity = np.eye(2, dtype=complex)

    # This has W(A) in the open unit disk because its numerical radius is 3/4.
    matrix_a = np.array([[0.0, 1.5], [0.0, 0.0]], dtype=complex)
    exterior_fields = []
    for point in circle:
        kernel = np.linalg.inv(identity - matrix_a / point)
        exterior_fields.append(kernel + kernel.conj().T)
    minimum_exterior_eigenvalue = min(
        np.linalg.eigvalsh(field).min() for field in exterior_fields
    )
    exterior_mass_error = np.linalg.norm(
        normalized_circle_integral(exterior_fields) - 2 * identity
    )

    # D is contractive and has spectral radius zero.  The Fourier moments are D^j.
    matrix_d = np.array([[0.0, 0.55], [0.0, 0.0]], dtype=complex)
    disk_fields = []
    for point in circle:
        resolvent = np.linalg.inv(identity - matrix_d / point)
        disk_fields.append(resolvent + resolvent.conj().T - identity)
    minimum_disk_eigenvalue = min(
        np.linalg.eigvalsh(field).min() for field in disk_fields
    )
    moment_errors = []
    for power in range(4):
        moment = normalized_circle_integral(
            [(point**power) * field for point, field in zip(circle, disk_fields)]
        )
        moment_errors.append(np.linalg.norm(moment - np.linalg.matrix_power(matrix_d, power)))

    tolerance = 2e-11
    assert minimum_exterior_eigenvalue >= -tolerance
    assert exterior_mass_error <= tolerance
    assert minimum_disk_eigenvalue >= -tolerance
    assert max(moment_errors) <= tolerance
    print(
        "PASS: min eig(E_A)=%.6g, mass error=%.3g, min eig(Phi_D)=%.6g, "
        "max moment error=%.3g"
        % (
            minimum_exterior_eigenvalue,
            exterior_mass_error,
            minimum_disk_eigenvalue,
            max(moment_errors),
        )
    )


if __name__ == "__main__":
    main()
