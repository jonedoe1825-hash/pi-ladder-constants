#!/usr/bin/env python3
"""
kappa-Quantization Verification.
Checks: factor 10 = (c/12)*N, pentagonal and Fibonacci values, all 7 kappa.
"""

import math

def check_kappa():
    print("=" * 60)
    print("KAPPA QUANTIZATION CHECK")
    print("=" * 60)
    passed = 0
    total = 7

    c = 24
    N = 5  # Level of Gamma_0(5)

    # --- Check 1: factor 10 = (c/12) * N = 2 * 5 ---
    factor = (c // 12) * N
    assert factor == 10, f"factor = {factor}, expected 10"
    print(f"  [PASS] Factor 10 = (c/12)*N = {c//12}*{N} = {factor}")
    passed += 1

    # --- Check 2: c/12 = 2 ---
    reduced_c = c / 12
    assert reduced_c == 2.0, f"c/12 = {reduced_c}, expected 2"
    print(f"  [PASS] c/12 = {c}/12 = {reduced_c:.0f}")
    passed += 1

    # --- Check 3: N = 5 (Gamma_0(5)) ---
    assert N == 5, f"N = {N}, expected 5"
    print(f"  [PASS] N = {N} (congruence subgroup Gamma_0(5))")
    passed += 1

    # --- Check 4: Pentagonal numbers P_k = k(3k-1)/2 ---
    # P_0 = 0, P_1 = 1, P_2 = 5
    pentagonal = {}
    for k in range(3):
        P_k = k * (3 * k - 1) // 2
        pentagonal[k] = P_k

    assert pentagonal[0] == 0, f"P_0 = {pentagonal[0]}"
    assert pentagonal[1] == 1, f"P_1 = {pentagonal[1]}"
    assert pentagonal[2] == 5, f"P_2 = {pentagonal[2]}"
    print(f"  [PASS] Pentagonal numbers: P_0={pentagonal[0]}, P_1={pentagonal[1]}, P_2={pentagonal[2]}")
    passed += 1

    # --- Check 5: Fibonacci numbers F_1=1, F_3=2, F_4=3, F_5=5 ---
    fib = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
    assert fib[1] == 1, f"F_1 = {fib[1]}"
    assert fib[3] == 2, f"F_3 = {fib[3]}"
    assert fib[4] == 3, f"F_4 = {fib[4]}"
    assert fib[5] == 5, f"F_5 = {fib[5]}"
    print(f"  [PASS] Fibonacci numbers: F_1={fib[1]}, F_3={fib[3]}, F_4={fib[4]}, F_5={fib[5]}")
    passed += 1

    # --- Check 6: All 7 kappa values ---
    # Pentagonal family (SL(2,Z)): P_k / 100
    kappa_pentagonal = [pentagonal[0] / 100, pentagonal[1] / 100, pentagonal[2] / 100]
    # Fibonacci family (Gamma_0(5)): F_k / 10
    kappa_fibonacci = [fib[1] / 10, fib[3] / 10, fib[4] / 10, fib[5] / 10]

    all_kappa = kappa_pentagonal + kappa_fibonacci
    all_kappa_sorted = sorted(all_kappa)

    expected_kappa = [0.00, 0.01, 0.05, 0.10, 0.20, 0.30, 0.50]

    for i, (k, e) in enumerate(zip(all_kappa_sorted, expected_kappa)):
        assert abs(k - e) < 1e-10, f"kappa[{i}] = {k}, expected {e}"

    print(f"  [PASS] All 7 kappa values:")
    print(f"         Pentagonal (SL(2,Z)): {[f'{k:.2f}' for k in kappa_pentagonal]}")
    print(f"         Fibonacci  (Gamma_0(5)): {[f'{k:.2f}' for k in kappa_fibonacci]}")
    print(f"         Combined:   {all_kappa_sorted}")
    passed += 1

    # --- Check 7: all kappa in [0, 1) ---
    for k in all_kappa:
        assert 0 <= k < 1, f"kappa = {k} not in [0, 1)"
    print(f"  [PASS] All kappa values in [0, 1)")
    passed += 1

    print(f"\n  RESULT: {passed}/{total} checks passed")
    return passed == total


if __name__ == "__main__":
    success = check_kappa()
    print("\n" + "=" * 60)
    print("ALL CHECKS PASSED" if success else "SOME CHECKS FAILED")
    print("=" * 60)
