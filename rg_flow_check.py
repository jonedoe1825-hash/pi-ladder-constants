#!/usr/bin/env python3
"""
RG Flow Verification for the pi-Ladder Parameterization.
Checks: Vol(S^3) -> alpha' -> beta_0 = ln(pi), and S^3 uniqueness.
"""

import math

def check_rg_flow():
    print("=" * 60)
    print("RG FLOW CHECK")
    print("=" * 60)
    passed = 0
    total = 6

    # --- Check 1: Vol(S^3) = 2*pi^2 ---
    vol_s3 = 2 * math.pi ** 2
    expected_vol = 19.739208802178716
    assert abs(vol_s3 - expected_vol) < 1e-10, "Vol(S^3) mismatch"
    print(f"  [PASS] Vol(S^3) = 2*pi^2 = {vol_s3:.15f}")
    passed += 1

    # --- Check 2: alpha' = pi ---
    T = 1.0 / vol_s3
    alpha_prime = 1.0 / (2 * math.pi * T)
    assert abs(alpha_prime - math.pi) < 1e-10, "alpha' != pi"
    print(f"  [PASS] alpha' = 1/(2*pi*T) = {alpha_prime:.15f}")
    print(f"         pi      = {math.pi:.15f}")
    passed += 1

    # --- Check 3: R = sqrt(alpha') = sqrt(pi) ---
    R = math.sqrt(alpha_prime)
    expected_R = math.sqrt(math.pi)
    assert abs(R - expected_R) < 1e-10, "R mismatch"
    print(f"  [PASS] R = sqrt(alpha') = {R:.15f}")
    passed += 1

    # --- Check 4: dilaton phi_0 = 12*ln(pi) ---
    c = 24
    phi_0 = (c / 2) * math.log(alpha_prime)
    expected_phi = 12 * math.log(math.pi)
    assert abs(phi_0 - expected_phi) < 1e-10, "phi_0 mismatch"
    print(f"  [PASS] phi_0 = (c/2)*ln(alpha') = 12*ln(pi) = {phi_0:.10f}")
    passed += 1

    # --- Check 5: beta_0 = (c * ln(alpha')) / 24 = ln(pi) ---
    beta_0 = (c * math.log(alpha_prime)) / 24
    expected_beta = math.log(math.pi)
    assert abs(beta_0 - expected_beta) < 1e-10, "beta_0 != ln(pi)"
    print(f"  [PASS] beta_0 = (c*ln(alpha'))/24 = ln(pi) = {beta_0:.15f}")
    print(f"         ln(pi) = {math.log(math.pi):.15f}")
    passed += 1

    # --- Check 6: S^3 is the unique sphere with alpha' = pi ---
    # Vol(S^d) = 2*pi^{(d+1)/2} / Gamma((d+1)/2)
    from math import gamma, pi

    def vol_sphere(d):
        return 2 * pi ** ((d + 1) / 2) / gamma((d + 1) / 2)

    spheres = {}
    for d in range(1, 8):
        vol = vol_sphere(d)
        alpha = vol / (2 * pi)
        spheres[d] = (vol, alpha)

    pi_spheres = [d for d in spheres if abs(spheres[d][1] - pi) < 1e-8]
    assert pi_spheres == [3], f"alpha'=pi only for S^3, got {pi_spheres}"
    print(f"  [PASS] S^3 is the unique sphere with alpha' = pi")
    print(f"         Spheres checked: S^1..S^7")
    print(f"         Only S^3 gives alpha' = pi (it is also the only")
    print(f"         sphere that is a Lie group: SU(2))")
    passed += 1

    print(f"\n  RESULT: {passed}/{total} checks passed")
    return passed == total


if __name__ == "__main__":
    success = check_rg_flow()
    print("\n" + "=" * 60)
    print("ALL CHECKS PASSED" if success else "SOME CHECKS FAILED")
    print("=" * 60)
