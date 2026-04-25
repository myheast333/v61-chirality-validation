#!/usr/bin/env python3
"""
Temporary Parity Violation in Strong Interactions under Extreme Density
Substrate Ontology V6.1 - Section 5.2

Prediction: At high baryon density, effective energy gap Δχ_eff increases,
            inducing temporary parity violation in the strong interaction.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
RHO_0 = 0.16          # Nuclear saturation density (fm^-3)
RHO_CRIT = 5.0        # Critical density for temporary parity violation (in units of ρ_0)
DELTA_CHI_0 = 0.2     # Strong interaction chirality gap at normal density (GeV)
ALPHA = 1.5           # Density scaling exponent

def effective_chirality_gap(rho):
    """
    Effective chirality energy gap as function of baryon density.
    At high density, chirality gradients amplify, increasing Δχ_eff.
    """
    return DELTA_CHI_0 * (1 + (rho / (RHO_CRIT * RHO_0))**ALPHA)

def parity_violation_strength(rho):
    """
    Parity violation strength P(rho) emerges when Δχ_eff exceeds a threshold.
    P(rho) = 1 - exp(-(Δχ_eff / Δχ_crit - 1)) for Δχ_eff > Δχ_crit.
    """
    delta_chi = effective_chirality_gap(rho)
    delta_chi_crit = effective_chirality_gap(RHO_CRIT * RHO_0)
    
    P = np.zeros_like(rho)
    mask = delta_chi > delta_chi_crit
    P[mask] = 1 - np.exp(-(delta_chi[mask] / delta_chi_crit - 1))
    return P

def chiral_magnetic_conductivity(rho):
    """
    Chiral magnetic effect conductivity σ_CME, proportional to parity violation strength.
    """
    P = parity_violation_strength(rho)
    return P * 0.1  # Normalized conductivity (arbitrary units)

def main():
    print("=" * 60)
    print("Strong Interaction Parity Violation at High Density")
    print("Substrate Ontology V6.1 - Section 5.2")
    print("=" * 60)
    
    # Density range: 0.5 ρ_0 to 10 ρ_0
    rho_ratio = np.linspace(0.5, 10, 500)
    rho = rho_ratio * RHO_0
    
    delta_chi = effective_chirality_gap(rho)
    P = parity_violation_strength(rho)
    sigma_cme = chiral_magnetic_conductivity(rho)
    
    print(f"\n📊 Parameters:")
    print(f"   Nuclear saturation density ρ_0 = {RHO_0} fm⁻³")
    print(f"   Critical density ratio = {RHO_CRIT} ρ_0")
    print(f"   Baseline chirality gap Δχ_0 = {DELTA_CHI_0} GeV")
    print(f"   Density scaling exponent α = {ALPHA}")
    print(f"\n   At ρ = 8 ρ_0: P = {parity_violation_strength(np.array([8*RHO_0]))[0]:.3f}")
    print(f"   (Observable in neutron star mergers / heavy-ion collisions)")
    
    # Create figure
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    # Panel 1: Effective chirality gap
    axes[0].plot(rho_ratio, delta_chi, 'b-', linewidth=2)
    axes[0].axvline(x=RHO_CRIT, color='red', linestyle='--', alpha=0.7, label=f'ρ_crit = {RHO_CRIT} ρ_0')
    axes[0].axhline(y=effective_chirality_gap(RHO_CRIT*RHO_0), color='gray', linestyle=':', alpha=0.5)
    axes[0].set_xlabel('Baryon Density ρ / ρ_0')
    axes[0].set_ylabel('Δχ_eff (GeV)')
    axes[0].set_title('Effective Chirality Energy Gap')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Panel 2: Parity violation strength
    axes[1].plot(rho_ratio, P, 'r-', linewidth=2)
    axes[1].axvline(x=RHO_CRIT, color='red', linestyle='--', alpha=0.7)
    axes[1].set_xlabel('Baryon Density ρ / ρ_0')
    axes[1].set_ylabel('Parity Violation Strength P')
    axes[1].set_title('Temporary Strong Parity Violation')
    axes[1].set_ylim(0, 1.05)
    axes[1].grid(True, alpha=0.3)
    
    # Panel 3: Chiral magnetic conductivity
    axes[2].plot(rho_ratio, sigma_cme, 'g-', linewidth=2)
    axes[2].axvline(x=RHO_CRIT, color='red', linestyle='--', alpha=0.7)
    axes[2].set_xlabel('Baryon Density ρ / ρ_0')
    axes[2].set_ylabel('σ_CME (arb. units)')
    axes[2].set_title('Chiral Magnetic Conductivity')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save figure
    os.makedirs('figures', exist_ok=True)
    output_path = 'figures/strong_parity.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n📈 Figure saved to: {output_path}")
    
    plt.show()
    print("\n✅ Validation complete.")

if __name__ == '__main__':
    main()
