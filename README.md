# Substrate Ontology V6.1: Chirality & Parity Restoration

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19574831.svg)](https://doi.org/10.5281/zenodo.19574831)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository provides the simulation code for **Substrate Ontology V6.1**, a theoretical framework that explains the origin of chirality and parity violation through a three-fold breaking mechanism.

> **"From Lattice Chirality to Weak Parity Violation — A Complete Microscopic Picture"**  
> Jingsong Zhou (April 2026)

The code in this repository specifically validates the two **high-energy physics predictions** from Sections 5.1 and 5.2 of the paper:

1.  **Parity Restoration in Weak Interactions at High Energy** (Section 5.1)
2.  **Temporary Parity Violation in Strong Interactions under Extreme Density** (Section 5.2)

## 📂 Repository Structure
v61-chirality-validation/
├── README.md # This file
├── requirements.txt # Python dependencies
├── parity_restoration.py # Simulation for Prediction 1 (Weak force)
├── strong_parity_density.py # Simulation for Prediction 2 (Strong force)
└── figures/ # Output directory for generated plots
├── parity_restoration.png
└── strong_parity.png


## 🚀 Quick Start

To reproduce the key figures from the paper, follow these steps:

1.  **Clone the repository and install dependencies**:
    ```bash
    git clone https://github.com/myheast333/v61-chirality-validation.git
    cd v61-chirality-validation
    pip install -r requirements.txt
    ```

2.  **Run the simulations**:
    ```bash
    # Simulate parity restoration in weak interactions
    python parity_restoration.py

    # Simulate temporary parity violation in strong interactions
    python strong_parity_density.py
    ```

3.  **View the results**: The scripts will generate publication-ready figures in the `figures/` directory.

## 🔮 Key Predictions & Validation

### Prediction 1: Weak Parity Restoration
- **What it is**: The left-handed preference of the weak force should gradually disappear as collision energies approach the electroweak scale (~246 GeV).
- **How to test**: Analyze data from future high-energy colliders (e.g., FCC-hh) for a decrease in parity-violating asymmetries.
- **Code**: `parity_restoration.py` implements the V6.1 prediction: `A(√s) = A₀ * exp(-(√s / Λ_EW)²)`.

### Prediction 2: Strong Parity Violation at High Density
- **What it is**: In extreme environments like neutron star cores or quark-gluon plasma, the strong force could exhibit temporary parity violation.
- **How to test**: Search for enhanced Chiral Magnetic Effect (CME) signals in heavy-ion collision data (e.g., from RHIC or LHC).
- **Code**: `strong_parity_density.py` models how baryon density amplifies the effective chirality gap, leading to a non-zero parity violation strength `P(ρ)`.

For a complete guide on experimental validation, please see the [`validation_protocol.md`](validation_protocol.md) file.

## 📖 Citation

If you use this code or its results, please cite the original paper:

```bibtex
@article{zhou2026chirality,
  title={Substrate Ontology V6.1: Chirality, Handedness, and Three-Fold Breaking},
  author={Zhou, Jingsong},
  year={2026},
  doi={10.5281/zenodo.19574831}
}
```
