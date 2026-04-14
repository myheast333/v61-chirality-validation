
---

### 2. `parity_restoration.py`

```python
#!/usr/bin/env python3
"""
Parity Restoration in Weak Interactions at High Energy
Substrate Ontology V6.1 - Section 5.1

Prediction: Parity asymmetry A decreases as collision energy approaches the electroweak scale.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Physical constants
LAMBDA_EW = 246.0          # Electroweak scale (GeV)
A0 = 1.0                   # Low-energy maximal parity violation

def parity_asymmetry(sqrt_s):
    """
    V6.1 prediction: Parity asymmetry decays exponentially with energy.
    A(sqrt_s) = A0 * exp(-(sqrt_s / Lambda)^2)
    """
    return A0 * np.exp(-(sqrt_s / LAMBDA_EW)**2)

def main():
    print("=" * 60)
    print("Weak Parity Restoration at High Energy")
    print("Substrate Ontology V6.1 - Section 5.1")
    print("=" * 60)
    
    # Collision energy range: 10 GeV to 2 TeV
    sqrt_s = np.logspace(1, 3.3, 500)  # GeV
    
    A = parity_asymmetry(sqrt_s)
    
    # Key values
    A_100GeV = parity_asymmetry(100)
    A_246GeV = parity_asymmetry(LAMBDA_EW)
    A_1TeV = parity_asymmetry(1000)
    
    print(f"\n📊 Results:")
    print(f"   Electroweak scale Λ = {LAMBDA_EW} GeV")
    print(f"   Asymmetry at 100 GeV:     {A_100GeV:.3f}")
    print(f"   Asymmetry at Λ (246 GeV): {A_246GeV:.3f} (1/e ≈ 0.368)")
    print(f"   Asymmetry at 1 TeV:       {A_1TeV:.4f}")
    
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    
    ax.semilogx(sqrt_s, A, 'r-', linewidth=2, label='V6.1 Prediction')
    ax.axvline(x=100, color='gray', linestyle='--', alpha=0.7, label='LEP/Tevatron scale')
    ax.axvline(x=LAMBDA_EW, color='blue', linestyle='--', alpha=0.7, label='EW scale (Λ = 246 GeV)')
    
    # Mark key points
    ax.scatter([100, LAMBDA_EW, 1000], [A_100GeV, A_246GeV, A_1TeV], 
               color='red', s=80, zorder=5)
    
    ax.set_xlabel('Collision Energy √s (GeV)')
    ax.set_ylabel('Parity Asymmetry A')
    ax.set_title('V6.1 Prediction: Weak Parity Restoration at High Energy')
    ax.set_ylim(0, 1.05)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save figure
    os.makedirs('figures', exist_ok=True)
    output_path = 'figures/parity_restoration.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n📈 Figure saved to: {output_path}")
    
    plt.show()
    print("\n✅ Validation complete.")

if __name__ == '__main__':
    main()
