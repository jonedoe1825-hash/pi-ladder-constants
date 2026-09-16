#!/usr/bin/env python3
"""pi_ladder_diagram.py - Schematic of the pi-ladder with the Omega-point.
Requires matplotlib: pip install matplotlib
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(8, 12))
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 13.5)
ax.set_aspect('equal')
ax.axis('off')

ax.text(0, 13.3, r'$\pi$-Ladder and the $\Omega$-Point',
        fontsize=16, ha='center', fontweight='bold')

omega_y = 12
ax.plot(0, omega_y, 'o', color='gold', ms=18, zorder=5)
ax.text(0.4, omega_y, r'$\Omega$ ($V \to 1$)', fontsize=13,
        va='center', fontweight='bold')
ax.text(0.4, omega_y - 0.4, 'IR fixed point', fontsize=9,
        va='center', style='italic')

steps = [
    (r'$s=+3$', r'$V \approx 0.999$', r'$y_t,\, V_{tb}$'),
    (r'$s=+2$', r'$V \approx 0.97$', r'$V_{cs}$'),
    (r'$s=+1$', r'$V \approx 0.84$', ''),
    (r'$s=0$', r'$V \approx 0.37$', 'separatrix'),
    (r'$s=-1$', r'$V \approx 0.07$', r'$\alpha$'),
    (r'$s=-2$', r'$V \approx 0.003$', r'$V_{ub},\, y_s$'),
    (r'$s=-3$', r'$V \approx 10^{-5}$', r'$y_u,\, y_d,\, y_e$'),
    (r'$s=-4$', r'$V \approx 10^{-14}$', r'$y_{\nu}$'),
    (r'$s=-5$', r'$V \approx 10^{-45}$', r'$\alpha_G$'),
]

ys = np.linspace(11, 1.5, len(steps))
for i, (sl, vl, cl) in enumerate(steps):
    y = ys[i]
    ax.plot([-2.2, 2.2], [y, y], '-', color='steelblue', lw=1.5, zorder=2)
    ax.text(-2.5, y, sl, fontsize=9, ha='right', va='center', color='steelblue')
    ax.text(2.5, y, vl, fontsize=8, ha='left', va='center', color='gray')
    if cl:
        ax.text(0, y - 0.25, cl, fontsize=7, ha='center',
                va='top', color='darkred', style='italic')

ax.annotate('', xy=(0, omega_y - 0.3), xytext=(0, 0.5),
            arrowprops=dict(arrowstyle='->', color='black', lw=2))

ax.annotate('', xy=(-0.15, omega_y - 0.15), xytext=(-1.5, 2),
            arrowprops=dict(arrowstyle='->', color='orange', lw=1.5,
                            connectionstyle='arc3,rad=0.3'))
ax.annotate('', xy=(0.15, omega_y - 0.15), xytext=(1.5, 2),
            arrowprops=dict(arrowstyle='->', color='green', lw=1.5,
                            connectionstyle='arc3,rad=-0.3'))
ax.text(-1.8, 5, r'Ray 1: $V \to 1$', fontsize=9, color='orange',
        rotation=70, ha='center')
ax.text(1.8, 5, r'Ray 2: $V \to 0$', fontsize=9, color='green',
        rotation=-70, ha='center')

ax.plot(0, 0.8, 's', color='darkred', ms=12, zorder=5)
ax.text(0.5, 0.8, 'UV frontier ($V \\to 0$)', fontsize=11,
        va='center', fontweight='bold')
ax.text(0.5, 0.35, 'asymptotic freedom', fontsize=9,
        va='center', style='italic')

ax.annotate(r'$\Lambda \sim 10^{-120}$' + '\n(double-log:\n' +
            r'$\Omega$ within $\Omega$)',
            xy=(2.2, 0.8), fontsize=8, ha='left', va='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                      alpha=0.8))

ft = (r'$V = \pi^{-(1/\pi)^s / n}$' + '\n\n' +
      r'$\mathcal{T}: x \mapsto \pi^x$' + '\n' +
      r'$\mathcal{T}^2(1) = \pi^\pi \approx 36.46$')
ax.text(-2.7, 7, ft, fontsize=10, ha='left', va='center',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.3))

plt.tight_layout()
plt.savefig('pi_ladder_omega_diagram.png', dpi=150, bbox_inches='tight')
print("Saved: pi_ladder_omega_diagram.png")
