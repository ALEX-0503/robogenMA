from __future__ import annotations

import streamlit as st


def inject_base_style() -> None:
    st.markdown(
        """
        <style>
        .main > div {
            padding-top: 1rem;
        }
        [data-testid="stAppViewContainer"] {
            background: #f8fafc;
        }
        .topbar {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .brand-wrap {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .brand-logo {
            width: 30px;
            height: 30px;
            border-radius: 8px;
            background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
        }
        .brand-title {
            margin: 0;
            font-size: 1.35rem;
            line-height: 1.1;
            color: #111827;
        }
        .brand-sub {
            margin: 0;
            color: #6b7280;
            font-size: 0.82rem;
        }
        .about-btn {
            border: 1px solid #e5e7eb;
            border-radius: 999px;
            padding: 5px 10px;
            font-size: 0.8rem;
            color: #111827;
            background: #ffffff;
        }
        .overview {
            background: #fcfcff;
            border: 1px solid #dbeafe;
            border-radius: 14px;
            padding: 14px;
            margin-bottom: 10px;
        }
        .overview h3 {
            margin: 0 0 4px 0;
            color: #111827;
            font-size: 1.25rem;
        }
        .overview p {
            margin: 0 0 10px 0;
            color: #6b7280;
        }
        .agent-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 10px;
        }
        .agent-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 10px;
        }
        .agent-card b {
            color: #111827;
        }
        .agent-card span {
            color: #6b7280;
            font-size: 0.8rem;
        }
        .flow-tabs {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 10px;
            margin-bottom: 14px;
        }
        .flow-tab {
            background: #f3f4f6;
            color: #4b5563;
            border-radius: 999px;
            text-align: center;
            padding: 6px 8px;
            font-size: 0.85rem;
            border: 1px solid transparent;
        }
        .flow-tab.active {
            background: #ffffff;
            color: #111827;
            border-color: #d1d5db;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        .panel {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 14px;
            padding: 14px;
            margin-bottom: 12px;
        }
        .panel h4 {
            margin: 0 0 6px 0;
            color: #111827;
        }
        .panel-sub {
            color: #6b7280;
            margin: 0 0 10px 0;
            font-size: 0.92rem;
        }
        .metric-row {
            border-top: 1px solid #f1f5f9;
            margin-top: 10px;
            padding-top: 10px;
        }
        .hint-box {
            background: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 10px;
            padding: 10px 12px;
            color: #1e3a8a;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_app_shell(active_tab: str) -> None:
    tabs = [
        ("Requirement Input", "requirement"),
        ("Parameter Display", "parameter"),
        ("Strategy & Simulation", "simulation"),
        ("Result Report", "report"),
    ]
    tabs_html = "".join(
        [
            f'<div class="flow-tab {"active" if active_tab == key else ""}">{label}</div>'
            for label, key in tabs
        ]
    )

    st.markdown(
        f"""
        <div class="topbar">
            <div class="brand-wrap">
                <div class="brand-logo">⚙</div>
                <div>
                    <h2 class="brand-title">RoboGenMA</h2>
                    <p class="brand-sub">Robotic General AI Manipulation Agent for Micro-Nano Soft Robots</p>
                </div>
            </div>
            <div class="about-btn">About System</div>
        </div>

        <div class="overview">
            <h3>System Overview</h3>
            <p>Automated pipeline from requirement input to strategy generation, simulation execution, and feedback optimization.</p>
            <div class="agent-grid">
                <div class="agent-card"><b>RK Agent</b><br><span>Requirement Parsing</span></div>
                <div class="agent-card"><b>CS Agent</b><br><span>Strategy Generation</span></div>
                <div class="agent-card"><b>SD Agent</b><br><span>Simulation Design</span></div>
                <div class="agent-card"><b>FO Agent</b><br><span>Execution Feedback</span></div>
            </div>
        </div>

        <div class="flow-tabs">
            {tabs_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

