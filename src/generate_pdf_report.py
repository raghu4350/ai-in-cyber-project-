import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import numpy as np

def create_pdf_report(output_pdf_path="report/AI_Cybersecurity_Unit1_Comprehensive_Report.pdf"):
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)
    print(f"[+] Generating Native PDF Report at: {output_pdf_path}...")
    
    with PdfPages(output_pdf_path) as pdf:
        # ----------------------------------------------------
        # PAGE 1: COVER & EXECUTIVE PROBLEM STATEMENT
        # ----------------------------------------------------
        fig = plt.figure(figsize=(8.5, 11))
        fig.patch.set_facecolor('#ffffff')
        
        # Header banner
        plt.subplot2grid((11, 1), (0, 0), rowspan=2)
        plt.axis('off')
        plt.text(0.5, 0.75, "AI-DRIVEN CYBER THREAT AWARENESS & DETECTION", 
                 ha='center', va='center', fontsize=18, fontweight='bold', color='#0f172a')
        plt.text(0.5, 0.45, "Comprehensive Technical Report & Academic Project Guide", 
                 ha='center', va='center', fontsize=12, fontweight='medium', color='#2563eb')
        plt.text(0.5, 0.15, "Course: AI in Cyber Security Lab (ENSP355) | K.R. Mangalam University | UNSW-NB15 Benchmark", 
                 ha='center', va='center', fontsize=9, color='#64748b', style='italic')
        plt.plot([0.05, 0.95], [0.02, 0.02], color='#cbd5e1', lw=1.5)
        
        # Section 1: Problem Statement
        plt.subplot2grid((11, 1), (2, 0), rowspan=9)
        plt.axis('off')
        
        text_content = """
1. THE PROBLEM STATEMENT (IN PLAIN WORDS)
--------------------------------------------------------------------------------------------------------
Every second, modern organizational networks process millions of packets: logins, video calls, 
emails, and database queries. Concealed inside this legitimate traffic are malicious cyber-threats:
• Exploits: Attackers weaponizing bugs (buffer overflows, SQLi) to seize server control.
• Denial of Service (DoS): Volumetric connection floods designed to paralyze server operations.
• Reconnaissance: Scanners (like Nmap) systematically mapping internal network ports.
• Backdoors & Shellcode: Stealth memory-injected payloads establishing remote command & control.

WHY TRADITIONAL DEFENSES (FIREWALLS & STATIC IDS) FAIL:
Traditional Intrusion Detection Systems (like classic Snort or static firewalls) rely on pre-defined
static signatures: "If packet payload contains exact hex string X from IP Y, block it."
Attackers trivially bypass this:
1. Polymorphic Malware: Changing a single byte in code alters the cryptographic hash completely.
2. Payload Obfuscation & Dynamic Ports: Evades static port matching and keyword searches.
3. Zero-Day Vulnerabilities: Brand-new attack methods have no pre-existing signature in databases.

THE AI BEHAVIORAL SOLUTION:
Instead of static text matching, AI analyzes traffic physics and behavioral telemetry:
• Connection duration, packet arrival frequency, and jitter (microsecond variances).
• Sent-to-received byte ratios and TCP handshake round-trip times.
• Time-To-Live (TTL) anomalies (e.g., standard Windows/Linux TTL vs. spoofed scanner TTL).
By learning baseline distributions of legitimate traffic vs. anomalous attack patterns, 
AI detects novel, zero-day attacks in near real-time.

THE DUAL OPERATIONAL CHALLENGE:
• False Negatives (FN): Missed attack -> leads to data breaches, ransomware, or server takeover.
• False Positives (FP): False alarm -> legitimate staff are blocked, creating a Self-Inflicted DoS.
"""
        plt.text(0.04, 0.96, text_content, ha='left', va='top', fontsize=9.2, fontfamily='monospace', linespacing=1.4)
        
        # Add visual callout box at bottom of page 1
        rect = plt.Rectangle((0.04, 0.05), 0.92, 0.22, fill=True, color='#eff6ff', ec='#3b82f6', lw=1.5)
        plt.gca().add_patch(rect)
        box_text = """CORE PROJECT OBJECTIVE:
Build, evaluate, and benchmark an end-to-end AI cyber threat detection pipeline comparing
Classical Supervised ML (Logistic Regression, Decision Trees, Random Forests) against Deep Learning
(Multi-Layer Perceptron), evaluating detection coverage (Recall), false alarms (FPR), training efficiency, 
real-time inference latency, operational threshold tuning, and algorithmic dataset bias."""
        plt.text(0.06, 0.24, box_text, ha='left', va='top', fontsize=8.8, fontweight='bold', color='#1e3a8a', linespacing=1.35)
        
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 2: THE 3 DATASETS & FEATURE TAXONOMY
        # ----------------------------------------------------
        fig = plt.figure(figsize=(8.5, 11))
        fig.patch.set_facecolor('#ffffff')
        
        plt.subplot2grid((11, 1), (0, 0), rowspan=1)
        plt.axis('off')
        plt.text(0.5, 0.7, "2. THE THREE DATASET FILES EXPLAINED (WHY 3 FILES?)", 
                 ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
        plt.plot([0.05, 0.95], [0.1, 0.1], color='#cbd5e1', lw=1.2)
        
        plt.subplot2grid((11, 1), (1, 0), rowspan=10)
        plt.axis('off')
        
        page2_text = """
The UNSW-NB15 benchmark was synthesized by the Australian Cyber Security Centre (ACCS) using an 
IXIA PerfectStorm rig to generate 100 GB of real modern normal traffic and 9 distinct attack types.

FILE BREAKDOWN & PURPOSE:
1. UNSW_NB15_training-set.csv (175,341 records | ~32.1 MB)
   • Role: Used strictly to train models and compute preprocessor parameters (scaler mean/variance).
   • Distribution: Normal Traffic = 56,000 (31.9%) | Malicious Traffic = 119,341 (68.1%).

2. UNSW_NB15_testing-set.csv (82,332 records | ~15.3 MB)
   • Role: Untouched blind evaluation benchmark. Kept strictly isolated during training.
   • Distribution: Normal Traffic = 37,000 (44.9%) | Malicious Traffic = 45,332 (55.1%).

3. UNSW-NB15_features.csv (44 Rows | ~3.2 KB)
   • Role: Feature metadata dictionary defining data types (float, integer, categorical) and groups.

WHY ARE THERE 3 DATASETS INSTEAD OF JUST ONE?
• Academic Standardization: Pre-defined train/test splits ensure all international research 
  compares models on the identical blind test set rather than differing random splits.
• Preventing Data Snooping: Preserves temporal integrity. Models cannot leak future packet statistics 
  into past training distributions.
• Feature Dictionary: Normalizes the technical schema across complex packet fields.

NETWORK FEATURES EXPLAINED IN SIMPLE TERMS (42 INPUT FEATURES):
1. Basic Features (dur, proto, service, state, spkts, dpkts, sbytes, dbytes, rate, sttl, dttl)
   • Quantifies connection duration, protocol (TCP/UDP), port service, packet and byte counts.
   • KEY INDICATOR: 'sttl' (Source Time-To-Live). Normal systems use 64 or 128. Automated attack 
     scanners frequently exhibit extreme, anomalous TTL values (e.g. 254).

2. Content & Payload Features (sload, dload, sloss, dloss, swin, dwin, smean, dmean)
   • Measures bits per second, packet drops (sloss), TCP window sizes, and mean packet sizes.
   • Detects buffer overflows (abnormally large smean) and DoS flooding (massive loss & load).

3. Time & Jitter Features (sinpkt, dinpkt, sjit, djit, tcprtt, synack, ackdat)
   • Measures microsecond delays between packets and 3-way handshake round-trip times.
   • Distinguishes irregular, bursty human traffic from automated, rigidly timed botnet attacks.

4. Generated Flow Features (ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm, ct_srv_dst)
   • Rolling historical connection counts tracking same IP/service across the last 100 flows.
   • Primary indicator for Port Scanning: 1 IP probing 90 different ports in 100 ms.
"""
        plt.text(0.04, 0.98, page2_text, ha='left', va='top', fontsize=9.1, fontfamily='monospace', linespacing=1.35)
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 3: PREPROCESSING & THE 9 ATTACK TYPES
        # ----------------------------------------------------
        fig = plt.figure(figsize=(8.5, 11))
        fig.patch.set_facecolor('#ffffff')
        
        plt.subplot2grid((11, 1), (0, 0), rowspan=1)
        plt.axis('off')
        plt.text(0.5, 0.7, "3. PREPROCESSING AUDIT & THE 9 CYBER ATTACK TYPES", 
                 ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
        plt.plot([0.05, 0.95], [0.1, 0.1], color='#cbd5e1', lw=1.2)
        
        plt.subplot2grid((11, 1), (1, 0), rowspan=10)
        plt.axis('off')
        
        page3_text = """
DATA PREPROCESSING: WHAT WAS DONE VS. WHAT WAS NOT DONE (AND WHY)
--------------------------------------------------------------------------------------------------------
[✓] DONE: Drop 'id' column
    -> Reason: 'id' is an arbitrary sequential counter. Leaving it in causes "shortcut learning" 
       where the model predicts attacks based on row index rather than packet physics.

[✓] DONE: Isolate 'attack_cat' from input feature matrix (X)
    -> Reason: 'attack_cat' explicitly labels the attack name ("DoS", "Exploit"). Leaving it in 
       causes target leakage. Preserved exclusively for Task 5 per-attack ethical bias auditing.

[✓] DONE: Median Imputation for missing values
    -> Reason: Network telemetry has extreme positive skew (a few flows send 10M bytes; most 
       send 500). Median prevents extreme outlier flows from distorting imputed values.

[✓] DONE: LabelEncoder on Categoricals ('proto', 'service', 'state')
    -> Reason: Converts string categories to consistent integers for linear and tree models.

[✓] DONE: StandardScaler (Fit on Train ONLY -> Transform Test)
    -> Reason: Prevents gradient explosion in Deep Learning & Logistic Regression. Crucially, 
       mean (μ) and variance (σ) are calculated solely on training data to prevent test leakage.

[✗] NOT DONE: Synthetic Oversampling (SMOTE)
    -> Reason: Synthetic packet generation distorts real network physics. Real enterprise networks 
       have rare attacks and abundant normal traffic; fake packets create massive false alarms.

[✗] NOT DONE: Retrospective Re-splitting of Train/Test sets
    -> Reason: Merging and shuffling would violate the official benchmark specification and 
       artificially inflate test accuracy by leaking temporal packet patterns.

THE 9 CYBER THREAT CATEGORIES IN THE DATASET:
1. Generic (33.6%): Cryptographic collision attacks and generic cipher evasion techniques.
2. Exploits (25.4%): Known vulnerability exploits targeting unpatched software servers.
3. Fuzzers (13.8%): Randomized, malformed packet bursts attempting to trigger buffer overflows.
4. DoS (9.3%): Volumetric connection flooding targeting service availability.
5. Reconnaissance (8.0%): Port scanning (Nmap) and network topology discovery probes.
6. Analysis (1.5%): Vulnerability scanning (port scans, web directory brute-forcing).
7. Backdoor (1.3%): Covert command & control channels bypassing inbound firewall rules.
8. Shellcode (0.9%): Executable binary payloads injected into vulnerable memory addresses.
9. Worms (0.1%): Self-propagating autonomous malware (rarest attack category).
"""
        plt.text(0.04, 0.98, page3_text, ha='left', va='top', fontsize=9.1, fontfamily='monospace', linespacing=1.35)
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 4: PIPELINE ARCHITECTURE & ROC CURVES
        # ----------------------------------------------------
        fig = plt.figure(figsize=(8.5, 11))
        fig.patch.set_facecolor('#ffffff')
        
        plt.subplot2grid((11, 1), (0, 0), rowspan=1)
        plt.axis('off')
        plt.text(0.5, 0.7, "4. FULL PIPELINE ARCHITECTURE & ROC CURVES", 
                 ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
        plt.plot([0.05, 0.95], [0.1, 0.1], color='#cbd5e1', lw=1.2)
        
        # Pipeline flowchart text representation
        plt.subplot2grid((11, 1), (1, 0), rowspan=4)
        plt.axis('off')
        pipeline_box = """
+---------------------------------------------------------------------------------------------------+
|                               END-TO-END SYSTEM PIPELINE ARCHITECTURE                             |
+---------------------------------------------------------------------------------------------------+
  [data/UNSW_NB15_training-set.csv] (175,341)         [data/UNSW_NB15_testing-set.csv] (82,332)
                          │                                           │
  [src/data_preprocessing.py]                                         │
  - Drop 'id' & isolate 'attack_cat'                                  │
  - LabelEncode ('proto', 'service', 'state')                         │
  - Fit StandardScaler on Train ONLY (μ, σ)                           │
                          │                                           │
                          ▼                                           ▼
                 Transformed X_train                         Transformed X_test
                          │                                           │
         ┌────────────────┴───────────────┐                           │
         ▼                                ▼                           │
  [Classical ML Models]           [Deep Learning MLP]                 │
  - Logistic Regression           - Layer 1: 128 ReLU                 │
  - Decision Tree (Depth=12)      - Layer 2: 64 ReLU                  │
  - Random Forest (100 Trees)     - Output: 1 Sigmoid (Adam)          │
         │                                │                           │
         └────────────────┬───────────────┘                           │
                          ▼                                           ▼
             [Trained Model Weights] ───────────────────────► [Blind Evaluation]
                                                              - Accuracy, Precision, Recall
                                                              - ROC-AUC, FPR, Latency
                                                                      │
                                                                      ▼
                                                              [Operational Tuning]
                                                              - Threshold sweep (τ=0.82)
                                                              - Per-attack bias audit
"""
        plt.text(0.04, 0.98, pipeline_box, ha='left', va='top', fontsize=7.8, fontfamily='monospace', linespacing=1.25)

        # Embed ROC Curve image if exists
        roc_img_path = "outputs/09_ml_roc_curves.png"
        if os.path.exists(roc_img_path):
            ax_roc = plt.subplot2grid((11, 1), (5, 0), rowspan=5)
            img = plt.imread(roc_img_path)
            ax_roc.imshow(img)
            ax_roc.axis('off')
            ax_roc.set_title("Figure 1: ROC Curves for Supervised Machine Learning Models (AUC Benchmark)", fontsize=10, fontweight='bold', pad=5)
            
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 5: ALL MODEL ACCURACY & ML VS DL COMPARISON
        # ----------------------------------------------------
        fig = plt.figure(figsize=(8.5, 11))
        fig.patch.set_facecolor('#ffffff')
        
        plt.subplot2grid((11, 1), (0, 0), rowspan=1)
        plt.axis('off')
        plt.text(0.5, 0.7, "5. MODEL ACCURACY BENCHMARK & WHY COMPARE ML VS. DL?", 
                 ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
        plt.plot([0.05, 0.95], [0.1, 0.1], color='#cbd5e1', lw=1.2)
        
        # Comparison Table
        plt.subplot2grid((11, 1), (1, 0), rowspan=4)
        plt.axis('off')
        table_text = """
EMPIRICAL BENCHMARK RESULTS (EVALUATED ON 82,332 UNTOUCHED TEST PACKETS):
========================================================================================================
Model Architecture      Accuracy  Precision  Recall (Coverage)  F1-Score  ROC-AUC    FPR   Latency(10k)
--------------------------------------------------------------------------------------------------------
Logistic Regression       80.44%     74.91%             96.95%    0.8452   0.9351  39.78%       1.70 ms
Decision Tree (Depth=12)  85.36%     80.72%             96.46%    0.8789   0.9625  28.23%       2.47 ms
Random Forest (Ensemble)  86.47%     80.81%             98.92%    0.8895   0.9831  28.78%      48.49 ms
Deep Learning (MLP 128x64)85.71%     80.89%             96.94%    0.8819   0.9686  28.06%      38.93 ms
========================================================================================================
CHAMPION MODEL: Random Forest achieved 98.92% Recall (missed only 1.08% of threats) & 0.9831 ROC-AUC.

WHY COMPARE ML VS DL? WHAT IS THE BENEFIT?
1. Structured Tabular Reality: Tree ensembles (Random Forest) systematically outperform Neural 
   Networks on structured network flow tables (Accuracy 86.47% vs. 85.71%; Recall 98.92% vs. 96.94%).
2. Training Cost Penalty: Decision Tree trained in 2.8s; Random Forest in 18.5s; while Deep Learning 
   MLP required 180.1s (60x slower) with zero accuracy gain.
3. Edge Firewall Deployment: Network firewalls (Cisco, Fortinet) run embedded CPUs. Decision Trees 
   evaluate in 2.47 ms per 10k packets using simple IF/ELSE branches. Deep Learning requires floating-
   point matrix multiplication, which chokes low-power line-rate gateways.
4. SOC Explainability: Decision Trees can be audited by analysts; Neural Networks are black boxes.
"""
        plt.text(0.04, 0.98, table_text, ha='left', va='top', fontsize=8.6, fontfamily='monospace', linespacing=1.3)

        # Embed ML vs DL plot
        mldl_img_path = "outputs/07_ml_vs_dl_comparison.png"
        if os.path.exists(mldl_img_path):
            ax_mldl = plt.subplot2grid((11, 1), (5, 0), rowspan=5)
            img = plt.imread(mldl_img_path)
            ax_mldl.imshow(img)
            ax_mldl.axis('off')
            ax_mldl.set_title("Figure 2: Empirical Benchmark - Accuracy, F1, Training Time & Latency", fontsize=10, fontweight='bold', pad=5)
            
        pdf.savefig(fig)
        plt.close()

        # ----------------------------------------------------
        # PAGE 6: ETHICAL SIMULATION & FILE WALKTHROUGH
        # ----------------------------------------------------
        fig = plt.figure(figsize=(8.5, 11))
        fig.patch.set_facecolor('#ffffff')
        
        plt.subplot2grid((11, 1), (0, 0), rowspan=1)
        plt.axis('off')
        plt.text(0.5, 0.7, "6. OPERATIONAL THRESHOLD TUNING & FILE DIRECTORY", 
                 ha='center', va='center', fontsize=14, fontweight='bold', color='#0f172a')
        plt.plot([0.05, 0.95], [0.1, 0.1], color='#cbd5e1', lw=1.2)
        
        plt.subplot2grid((11, 1), (1, 0), rowspan=10)
        plt.axis('off')
        
        page6_text = """
THE FALSE ALARM CRISIS AT DEFAULT THRESHOLD (τ = 0.50):
At τ = 0.50, the False Positive Rate is 28.78%. Out of 37,000 legitimate normal sessions in the 
test set, 10,648 real users are blocked! In a hospital or university, shutting down 28% of innocent 
users causes operational paralysis and analyst alert fatigue.

OPERATIONAL THRESHOLD TUNING (τ = 0.82):
By shifting the classification probability threshold from τ = 0.50 -> 0.82:
• False Positive Rate drops from 28.78% down to 5.57% (a 5x reduction in false alarms!).
• Precision jumps from 80.81% to 95.22% (analysts can trust that alerts are genuine).
• Security Detection Coverage remains high at 90.67% Recall.

DATASET BIAS AUDIT (PER-ATTACK RECALL ON TEST SET):
• Generic: 100.0% (18,871/18,871)     • Reconnaissance: 99.94% (3,494/3,496)
• Exploits: 99.69% (11,098/11,132)    • Backdoor: 100.0% (583/583)
• DoS: 99.90% (4,085/4,089)           • Worms: 100.0% (44/44)
• Fuzzers (The Vulnerable Class): 92.73% (441 missed packets due to mutated payload mimicry).

COMPLETE REPOSITORY FILE GUIDE:
• src/main.py: Master orchestrator executing Tasks 1-5 end-to-end with a single command.
• src/data_preprocessing.py: Implements load_data(), median fillna, LabelEncoder & StandardScaler.
• src/eda_analysis.py: Generates threat distributions, protocol plots, KDE curves & feature importances.
• src/ml_models.py: Trains Logistic Regression, Decision Tree & Random Forest with ROC evaluation.
• src/dl_models.py: Multi-Layer Perceptron (128x64 units) with Adam optimizer & comparison plots.
• src/ethical_sim.py: Simulates threshold trade-offs & audits per-attack detection bias.
• src/validate_env.py: Diagnostic script verifying Python, dependencies, and dataset integrity.
• notebooks/UNSW_NB15_Analysis.ipynb: Interactive lab notebook with code, outputs & embedded charts.
• outputs/best_threat_detector_rf.joblib: Serialized Random Forest model ready for live deployment.
• report/COMPREHENSIVE_PROJECT_REPORT.html: Styled offline HTML report.
• report/AI_Cybersecurity_Unit1_Comprehensive_Report.pdf: This native multi-page PDF document.
"""
        plt.text(0.04, 0.98, page6_text, ha='left', va='top', fontsize=8.6, fontfamily='monospace', linespacing=1.35)
        pdf.savefig(fig)
        plt.close()
        
    print(f"[OK] Successfully generated 6-Page PDF Report at: {output_pdf_path}")
    return True

if __name__ == "__main__":
    create_pdf_report()
