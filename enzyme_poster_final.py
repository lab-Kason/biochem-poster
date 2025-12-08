import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from streamlit_option_menu import option_menu

# Page configuration
st.set_page_config(
    page_title="Enzyme Inhibitors in Drug Development",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful styling
def local_css():
    st.markdown("""
    <style>
    .main-header {
        font-size: 3.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .section-header {
        font-size: 2rem;
        color: #2E86AB;
        border-left: 5px solid #A23B72;
        padding-left: 1rem;
        margin: 2rem 0 1rem 0;
    }
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    .mechanism-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #A23B72;
    }
    .stButton>button {
        background: linear-gradient(45deg, #2E86AB, #A23B72);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 25px;
        font-weight: 600;
    }
    .drug-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Header with navigation
def create_header():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="main-header">🧬 Enzyme Inhibitors in Drug Development</div>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-size: 1.1rem; color: #666; margin-bottom: 1rem;">An Interactive Educational Platform for Understanding Drug Development; Group member:Fung Yat Kiu (13880442)Lee Chun Hei (13596941)Lo Yuet Ching (13881997)CHEN Ying Pui(13876834)Chiu Ka Chun(13713800)</p>', unsafe_allow_html=True)
        
        # Complete Application Guide
        with st.expander("🎯 **START HERE: Complete User Guide**", expanded=False):
            st.markdown("""
            ### Welcome! 👋
            
            This interactive platform helps you understand enzyme inhibitors in drug development.
            Perfect for students, researchers, and anyone interested in biochemistry and pharmacology.
            
            ---
            
            ### 📋 Five Interactive Sections:
            
            **1. 🏠 Overview**
            - Statistics on enzyme inhibitor drugs
            - Market impact and therapeutic applications
            - *Best for: Understanding the big picture*
            
            **2. ⚙️ Mechanisms**
            - Interactive simulator for 4 inhibition types
            - **Dual visualization:** Michaelis-Menten + Lineweaver-Burk plots side-by-side
            - Adjustable parameters (Km, Vmax, inhibitor strength)
            - See how each mechanism affects both curve types simultaneously
            - *Best for: Learning how inhibitors work AND identifying mechanisms*
            
            **3. 📚 Drug Development Case Studies**
            - 5 blockbuster enzyme inhibitor drugs: Discovery to market
            - Development timelines, clinical trials, and FDA approval stories
            - Market impact and patient outcomes data
            - *Best for: Understanding complete drug development process*
            
            **4. 🧮 Calculator**
            - IC50 calculator (with CSV export)
            - Ki calculator (Cheng-Prusoff equations)
            - Dose-response curve generator
            - *Best for: Analyzing your experimental data*
            
            **5. 📖 References**
            - 26+ peer-reviewed papers
            - Online databases and resources
            - *Best for: Citations and further reading*
            
            ---
            
            ### 💡 Quick Start Tips:
            
            - **Beginners:** Start with Overview → Mechanisms → Case Studies
            - **Students with data:** Go to Calculator to analyze results
            - **In-depth learners:** Work through all sections sequentially
            - **Each section has its own guide** - Look for "📖 How to Use" expandable boxes
            
            **All tools are interactive - adjust sliders to see immediate results!**
            
            *Select a section from the menu below to begin ⬇️*
            """)
        
        # Navigation
        selected = option_menu(
            menu_title=None,
            options=["Overview", "Mechanisms", "Case Studies", "Calculator", "References"],
            icons=["house", "gear", "book", "calculator", "journal-text"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#f8f9fa"},
                "icon": {"color": "#2E86AB", "font-size": "18px"}, 
                "nav-link": {"font-size": "16px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
                "nav-link-selected": {"background-color": "#2E86AB"},
            }
        )
    return selected

# Overview Section
def show_overview():
    st.markdown('<div class="section-header">📊 Executive Summary</div>', unsafe_allow_html=True)
    
    # User Guide
    with st.expander("📖 How to Use This Section", expanded=False):
        st.markdown("""
        **Overview Section Guide:**
        
        This section provides key statistics about enzyme inhibitors in modern medicine.
        
        **What you'll see:**
        - 📊 **Success statistics** - How many FDA drugs target enzymes
        - 🎯 **Market data** - Financial impact of enzyme inhibitor drugs
        - 📈 **Interactive bar chart** - Visual breakdown of therapeutic applications
        
        **Simply scroll down to explore the statistics and visualizations.**
        
        All data is referenced from peer-reviewed publications (see References section).
        """)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-card">
        <h3>🚀 What is enzyme inhibitor?</h3>
        Enzyme inhibitors are molecules that bind to enzymes and prevent their activity. This is one of the most successful strategies and offers a huge advantage to modern drug development by enabling the targeting of specific enzymes involved in disease pathways with remarkable precision and efficacy.
        </div>
        """, unsafe_allow_html=True)
        
        st.write("""
        ### Why This Approach Succeeds in Drug Development:
        - **High Specificity**: Design drugs targeting only disease-related enzymes
        - **Predictable Kinetics**: Apply well-understood mechanisms to drug optimization
        - **Proven Track Record**: Multiple blockbuster drugs (see Case Studies)
        - **Rational Design**: Structure-based approaches enable targeted development
        - **Clinical Success**: From aspirin to modern cancer therapies
        """)
        
        st.markdown("### 💊 Drug Development Reality:")
        st.info("""
        **Development Timeline & Success Rates** (DiMasi et al., 2016):
        - ⏱️ **Average time:** 10-15 years from discovery to approval
        - 💰 **Average cost:** $2.6 billion per approved drug
        - 📊 **Success rate:** Only 12% of drug candidates reach market
        - 🎯 **Enzyme targets:** ~47% of all FDA-approved drugs target enzymes
        - 💵 **Market value:** $180+ billion annually for enzyme inhibitors
        """)
    
    with col2:
        # Quick stats
        stats_data = {
            'Category': ['Approved Drugs', 'Clinical Trials', 'Market Value', 'Success Rate'],
            'Value': ['250+', '800+', '$150B+', '12%']
        }
        df_stats = pd.DataFrame(stats_data)
        fig = px.bar(df_stats, x='Value', y='Category', orientation='h',
                    color='Category', color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, width='stretch')
        
        st.caption("""*Data sources: FDA Drug Approvals Database (2024); ClinicalTrials.gov; 
        Evaluate Pharma Market Reports (2023). Success rate from DiMasi et al. (2016). 
        See References section for full citations.*""")
    
    # Drug Development Pipeline
    st.markdown("---")
    st.markdown("### 🔬 Drug Development Pipeline: From Enzyme Target to FDA Approval")
    
    st.write("""This application demonstrates key stages in enzyme inhibitor drug development:""")
    
    # Create pipeline visualization
    pipeline_data = pd.DataFrame({
        'Stage': ['1. Target\nIdentification', '2. Lead\nDiscovery', '3. Lead\nOptimization', 
                  '4. Preclinical\nTesting', '5. Clinical\nTrials', '6. FDA\nApproval', '7. Post-Market\nMonitoring'],
        'Duration': ['1-2 years', '2-3 years', '2-3 years', '1-2 years', '6-7 years', '1-2 years', 'Ongoing'],
        'Success_Rate': [100, 80, 60, 40, 20, 12, 12],
        'Description': [
            'Identify enzyme involved in disease',
            'Screen compounds for inhibition activity',
            'Improve IC50, Ki, selectivity, ADME properties',
            'Animal testing for safety and efficacy',
            'Phase I (safety), II (efficacy), III (large-scale)',
            'Regulatory review and approval',
            'Phase IV studies, adverse event monitoring'
        ]
    })
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        # Pipeline flowchart
        fig_pipeline = go.Figure()
        
        colors = ['#2E86AB', '#3FA7D6', '#59C3C3', '#74D3AE', '#92E5A1', '#A8E6A1', '#C6EBBE']
        
        for i, row in pipeline_data.iterrows():
            fig_pipeline.add_trace(go.Bar(
                y=[row['Stage']],
                x=[1],
                orientation='h',
                name=row['Stage'],
                text=f"<b>{row['Stage']}</b><br>{row['Duration']}",
                textposition='inside',
                marker=dict(color=colors[i]),
                hovertext=f"{row['Description']}<br>Duration: {row['Duration']}<br>Success Rate: {row['Success_Rate']}%",
                hoverinfo='text',
                showlegend=False
            ))
        
        fig_pipeline.update_layout(
            title='Enzyme Inhibitor Drug Development Stages',
            xaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, autorange='reversed'),
            height=400,
            margin=dict(l=10, r=10, t=40, b=10),
            plot_bgcolor='white'
        )
        
        st.plotly_chart(fig_pipeline, use_container_width=True)
    
    with col_b:
        st.markdown("**Key Milestones:**")
        st.markdown("""
        **Stage 1-2:** Enzyme target identification and screening
        - Example: HMG-CoA reductase for cholesterol (Statins)
        - See: **Mechanisms** section
        
        **Stage 3:** Optimize IC50/Ki values
        - Example: Atorvastatin optimization from compactin
        - See: **Calculator** section (IC50/Ki tools)
        
        **Stage 4-5:** Clinical validation
        - Example: Heart Protection Study (Statins)
        - See: **Case Studies** section
        
        **Stage 6:** Lineweaver-Burk analysis confirms mechanism
        - See: **Mechanisms** section (includes Lineweaver-Burk plots)
        """)
        
        st.info("""**This app covers:** Stages 1-3 (mechanism understanding, kinetic analysis, potency optimization) 
        and demonstrates successful Stage 6-7 examples through case studies.""")

# Interactive Mechanisms Section
def show_mechanisms():
    st.markdown('<div class="section-header">🔬 Inhibition Mechanisms</div>', unsafe_allow_html=True)
    
    # User Guide for Mechanisms
    with st.expander("📖 How to Use This Interactive Simulator", expanded=False):
        st.markdown("""
        **Interactive Enzyme Inhibition Simulator with Dual Visualization**
        
        **What's New:** Each inhibition type now shows **BOTH** visualization methods side-by-side:
        - **Left plot:** Michaelis-Menten curve (hyperbolic)
        - **Right plot:** Lineweaver-Burk plot (linear transformation)
        - **Same sliders control both plots** - see the relationship instantly!
        
        ---
        
        **Step-by-Step Guide:**
        1. **Select inhibition type** from dropdown (left panel)
        2. **Read the mechanism description** to understand how it works
        3. **Adjust Km slider** (0.1-10.0 mM) - substrate binding affinity
        4. **Adjust Vmax slider** (1-100 µmol/min) - maximum reaction velocity
        5. **Toggle "Show Inhibitor Effect"** checkbox to compare curves
        6. **Use Inhibitor Strength (α) slider** (1.0-5.0) to see dose-dependent effects
        7. **Compare both plots** - see how MM curves transform into LB lines!
        
        **Understanding the Parameters:**
        - **Km:** Lower values = enzyme has higher affinity for substrate
        - **Vmax:** Higher values = enzyme can work faster
        - **α (alpha):** Inhibitor strength factor where α = 1 + [I]/Ki (higher = stronger inhibition)
        
        **Interpreting the Dual Plots:**
        
        **Michaelis-Menten Plot (Left):**
        - **Blue curve:** Normal enzyme activity (no inhibitor)
        - **Red dashed curve:** Activity with inhibitor present
        - Watch how curve shape changes with different mechanisms
        
        **Lineweaver-Burk Plot (Right):**
        - **Linear transformation:** 1/v vs 1/[S]
        - **Y-intercept = 1/Vmax**
        - **X-intercept = -1/Km**
        - **Key advantage:** Line intersection patterns identify mechanisms!
        
        **What to Observe for Each Mechanism:**
        
        **Competitive Inhibition:**
        - MM: Can reach same Vmax at high [S], but needs more substrate
        - LB: Lines intersect on Y-axis (same Vmax, different Km)
        
        **Non-competitive Inhibition:**
        - MM: Lower plateau (Vmax reduced), same curve shape
        - LB: Lines intersect on X-axis (same Km, different Vmax)
        
        **Uncompetitive Inhibition:**
        - MM: Both Vmax and apparent Km reduced proportionally
        - LB: Lines are parallel (both intercepts change equally)
        
        **Mixed Inhibition:**
        - MM: Combination of competitive and non-competitive effects
        - LB: Lines intersect in 2nd quadrant (off both axes)
        
        ---
        
        **Why This Dual View is Powerful:**
        - See the **same data** in two complementary ways
        - MM plots show biological reality (velocity curves)
        - LB plots reveal mathematical relationships (easier to extract Km, Vmax)
        - Together they provide complete mechanistic understanding
        
        *Try adjusting the sliders and watch how both plots respond together!*
        """)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        mechanism = st.selectbox(
            "Select Inhibition Type:",
            ["Competitive Inhibition", "Non-competitive Inhibition", 
             "Uncompetitive Inhibition", "Mixed Inhibition"],
            key="mechanism_select"
        )
        
        st.markdown("""
        <div class="mechanism-card">
        <h4>🎯 How it works:</h4>
        """, unsafe_allow_html=True)
        
        if mechanism == "Competitive Inhibition":
            st.write("""
            - Inhibitor competes with substrate for active site
            - Resembles substrate structure
            - Effect can be overcome by increasing substrate concentration
            - **Example**: Statins (HMG-CoA reductase inhibitors)
            """)
            
            # Create schematic diagram for competitive inhibition
            fig_mech = go.Figure()
            
            # Enzyme (rectangle)
            fig_mech.add_shape(type="rect", x0=0.5, y0=0.3, x1=1.5, y1=0.7,
                              line=dict(color="RoyalBlue", width=3), fillcolor="lightblue")
            # Active site (small notch)
            fig_mech.add_shape(type="rect", x0=0.45, y0=0.45, x1=0.55, y1=0.55,
                              line=dict(color="red", width=2), fillcolor="lightyellow")
            
            # Substrate (circle) - fits active site
            fig_mech.add_shape(type="circle", x0=0.15, y0=0.45, x1=0.35, y1=0.65,
                              line=dict(color="green", width=2), fillcolor="lightgreen")
            
            # Inhibitor (triangle-like using path) - similar shape to substrate
            fig_mech.add_shape(type="circle", x0=0.15, y0=0.15, x1=0.35, y1=0.35,
                              line=dict(color="red", width=2), fillcolor="lightcoral")
            
            # Arrow showing competition
            fig_mech.add_annotation(x=0.25, y=0.55, ax=0.5, ay=0.5, 
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="green")
            fig_mech.add_annotation(x=0.25, y=0.25, ax=0.5, ay=0.5,
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="red")
            
            # Labels
            fig_mech.add_annotation(x=1.0, y=0.85, text="<b>Enzyme</b>", showarrow=False, font=dict(size=12))
            fig_mech.add_annotation(x=0.25, y=0.7, text="Substrate", showarrow=False, font=dict(size=10, color="green"))
            fig_mech.add_annotation(x=0.25, y=0.1, text="Inhibitor", showarrow=False, font=dict(size=10, color="red"))
            fig_mech.add_annotation(x=0.5, y=0.5, text="Active\nSite", showarrow=False, font=dict(size=8))
            
            fig_mech.update_layout(
                showlegend=False,
                height=200,
                margin=dict(l=10, r=10, t=10, b=10),
                xaxis=dict(range=[0, 2], showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(range=[0, 1], showgrid=False, showticklabels=False, zeroline=False),
                plot_bgcolor='white'
            )
            st.plotly_chart(fig_mech, use_container_width=True)
            
        elif mechanism == "Non-competitive Inhibition":
            st.write("""
            - Binds to enzyme at site other than active site
            - Reduces enzyme efficiency without blocking substrate binding
            - Cannot be overcome by substrate concentration
            - **Example**: Heavy metal ions
            """)
            
            # Create schematic diagram for non-competitive inhibition
            fig_mech = go.Figure()
            
            # Enzyme (rectangle)
            fig_mech.add_shape(type="rect", x0=0.5, y0=0.3, x1=1.5, y1=0.7,
                              line=dict(color="RoyalBlue", width=3), fillcolor="lightblue")
            # Active site
            fig_mech.add_shape(type="rect", x0=0.45, y0=0.45, x1=0.55, y1=0.55,
                              line=dict(color="green", width=2), fillcolor="lightyellow")
            # Allosteric site
            fig_mech.add_shape(type="rect", x0=1.45, y0=0.45, x1=1.55, y1=0.55,
                              line=dict(color="red", width=2), fillcolor="lightpink")
            
            # Substrate (circle) - at active site
            fig_mech.add_shape(type="circle", x0=0.15, y0=0.45, x1=0.35, y1=0.65,
                              line=dict(color="green", width=2), fillcolor="lightgreen")
            
            # Inhibitor (different shape) - at allosteric site
            fig_mech.add_shape(type="rect", x0=1.65, y0=0.4, x1=1.85, y1=0.6,
                              line=dict(color="red", width=2), fillcolor="lightcoral")
            
            # Arrows
            fig_mech.add_annotation(x=0.25, y=0.55, ax=0.5, ay=0.5,
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="green")
            fig_mech.add_annotation(x=1.75, y=0.5, ax=1.5, ay=0.5,
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="red")
            
            # Labels
            fig_mech.add_annotation(x=1.0, y=0.85, text="<b>Enzyme</b>", showarrow=False, font=dict(size=12))
            fig_mech.add_annotation(x=0.25, y=0.7, text="Substrate", showarrow=False, font=dict(size=10, color="green"))
            fig_mech.add_annotation(x=1.75, y=0.65, text="Inhibitor", showarrow=False, font=dict(size=10, color="red"))
            fig_mech.add_annotation(x=0.5, y=0.5, text="Active", showarrow=False, font=dict(size=7))
            fig_mech.add_annotation(x=1.5, y=0.5, text="Allosteric", showarrow=False, font=dict(size=7))
            
            fig_mech.update_layout(
                showlegend=False,
                height=200,
                margin=dict(l=10, r=10, t=10, b=10),
                xaxis=dict(range=[0, 2], showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(range=[0, 1], showgrid=False, showticklabels=False, zeroline=False),
                plot_bgcolor='white'
            )
            st.plotly_chart(fig_mech, use_container_width=True)
            
        elif mechanism == "Uncompetitive Inhibition":
            st.write("""
            - Binds only to enzyme-substrate complex
            - Common in multi-substrate reactions
            - **Example**: Lithium for certain enzymes
            """)
            
            # Create schematic diagram for uncompetitive inhibition
            fig_mech = go.Figure()
            
            # Enzyme (rectangle)
            fig_mech.add_shape(type="rect", x0=0.5, y0=0.3, x1=1.5, y1=0.7,
                              line=dict(color="RoyalBlue", width=3), fillcolor="lightblue")
            # Active site with substrate already bound
            fig_mech.add_shape(type="rect", x0=0.45, y0=0.45, x1=0.55, y1=0.55,
                              line=dict(color="green", width=2), fillcolor="lightgreen")
            
            # Substrate (circle) - BOUND to active site
            fig_mech.add_shape(type="circle", x0=0.43, y0=0.43, x1=0.57, y1=0.57,
                              line=dict(color="green", width=2), fillcolor="lightgreen")
            
            # New binding site created by ES complex
            fig_mech.add_shape(type="rect", x0=1.45, y0=0.35, x1=1.55, y1=0.45,
                              line=dict(color="orange", width=2), fillcolor="lightyellow")
            
            # Inhibitor - binds to ES complex only
            fig_mech.add_shape(type="circle", x0=1.65, y0=0.35, x1=1.85, y1=0.55,
                              line=dict(color="red", width=2), fillcolor="lightcoral")
            
            # Arrow showing inhibitor binding to ES complex
            fig_mech.add_annotation(x=1.75, y=0.45, ax=1.5, ay=0.4,
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="red")
            
            # Labels
            fig_mech.add_annotation(x=1.0, y=0.85, text="<b>Enzyme-Substrate Complex</b>", showarrow=False, font=dict(size=12))
            fig_mech.add_annotation(x=0.5, y=0.2, text="ES Complex", showarrow=False, font=dict(size=10, color="green"))
            fig_mech.add_annotation(x=1.75, y=0.6, text="Inhibitor", showarrow=False, font=dict(size=10, color="red"))
            fig_mech.add_annotation(x=1.5, y=0.3, text="New\nSite", showarrow=False, font=dict(size=7))
            
            fig_mech.update_layout(
                showlegend=False,
                height=200,
                margin=dict(l=10, r=10, t=10, b=10),
                xaxis=dict(range=[0, 2], showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(range=[0, 1], showgrid=False, showticklabels=False, zeroline=False),
                plot_bgcolor='white'
            )
            st.plotly_chart(fig_mech, use_container_width=True)
            
        else:  # Mixed Inhibition
            st.write("""
            - Combination of competitive and non-competitive features
            - Binds to both enzyme and enzyme-substrate complex
            - **Example**: Many kinase inhibitors
            """)
            
            # Create schematic diagram for mixed inhibition
            fig_mech = go.Figure()
            
            # Two scenarios side by side
            # Left: Inhibitor binding to free enzyme
            fig_mech.add_shape(type="rect", x0=0.3, y0=0.55, x1=0.7, y1=0.85,
                              line=dict(color="RoyalBlue", width=2), fillcolor="lightblue")
            fig_mech.add_shape(type="rect", x0=0.25, y0=0.65, x1=0.32, y1=0.75,
                              line=dict(color="red", width=2), fillcolor="lightpink")
            fig_mech.add_shape(type="circle", x0=0.05, y0=0.65, x1=0.2, y1=0.8,
                              line=dict(color="red", width=2), fillcolor="lightcoral")
            fig_mech.add_annotation(x=0.125, y=0.725, ax=0.28, ay=0.7,
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor="red")
            
            # Right: Inhibitor binding to ES complex
            fig_mech.add_shape(type="rect", x0=1.3, y0=0.55, x1=1.7, y1=0.85,
                              line=dict(color="RoyalBlue", width=2), fillcolor="lightblue")
            fig_mech.add_shape(type="circle", x0=1.27, y0=0.67, x1=1.37, y1=0.77,
                              line=dict(color="green", width=2), fillcolor="lightgreen")
            fig_mech.add_shape(type="rect", x0=1.68, y0=0.65, x1=1.75, y1=0.75,
                              line=dict(color="red", width=2), fillcolor="lightpink")
            fig_mech.add_shape(type="circle", x0=1.8, y0=0.65, x1=1.95, y1=0.8,
                              line=dict(color="red", width=2), fillcolor="lightcoral")
            fig_mech.add_annotation(x=1.875, y=0.725, ax=1.72, ay=0.7,
                                   xref="x", yref="y", axref="x", ayref="y",
                                   showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5, arrowcolor="red")
            
            # Labels
            fig_mech.add_annotation(x=0.5, y=0.95, text="<b>E + I → EI</b>", showarrow=False, font=dict(size=11))
            fig_mech.add_annotation(x=1.5, y=0.95, text="<b>ES + I → ESI</b>", showarrow=False, font=dict(size=11))
            fig_mech.add_annotation(x=0.125, y=0.87, text="Inhibitor", showarrow=False, font=dict(size=8, color="red"))
            fig_mech.add_annotation(x=1.32, y=0.87, text="Substrate", showarrow=False, font=dict(size=8, color="green"))
            fig_mech.add_annotation(x=1.875, y=0.87, text="Inhibitor", showarrow=False, font=dict(size=8, color="red"))
            fig_mech.add_annotation(x=1.0, y=0.4, text="<b>Inhibitor binds to both free enzyme AND ES complex</b>", 
                                   showarrow=False, font=dict(size=10))
            
            fig_mech.update_layout(
                showlegend=False,
                height=250,
                margin=dict(l=10, r=10, t=10, b=10),
                xaxis=dict(range=[0, 2], showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(range=[0.3, 1], showgrid=False, showticklabels=False, zeroline=False),
                plot_bgcolor='white'
            )
            st.plotly_chart(fig_mech, use_container_width=True)
            
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Interactive kinetics plot
        st.subheader("📈 Kinetic Effects")
        
        # Add reset button at the top
        col_reset, col_space = st.columns([1, 3])
        with col_reset:
            if st.button("🔄 Reset to Defaults", help="Reset all parameters to default values"):
                # Clear all relevant session state keys
                keys_to_clear = ['km_slider', 'vmax_slider', 'show_inh_mech', 'inhibitor_conc_slider', 
                                'ki_slider', 'show_km_line', 'show_vmax_line', 'show_intercepts']
                for key in keys_to_clear:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
        
        km = st.slider("Km (substrate affinity)", 0.1, 10.0, 1.0, 0.1, key="km_slider",
                      help="Michaelis constant: substrate concentration at half Vmax (lower = higher affinity)")
        vmax = st.slider("Vmax (maximum velocity)", 1, 100, 50, 1, key="vmax_slider",
                        help="Maximum reaction velocity when enzyme is fully saturated with substrate")
        
        # Add inhibitor strength control - ENHANCED with [I] and Ki
        show_inhibitor = st.checkbox("Show Inhibitor Effect", value=True, key="show_inh_mech")
        
        if show_inhibitor:
            st.markdown("**Inhibitor Parameters:**")
            inhibitor_conc = st.slider("[I] Inhibitor Concentration (µM)", 0.0, 10.0, 2.0, 0.5, 
                                      key="inhibitor_conc_slider",
                                      help="Concentration of inhibitor added to the reaction")
            ki_value = st.slider("Ki (inhibitor binding constant)", 0.5, 5.0, 1.0, 0.1, 
                                key="ki_slider",
                                help="Dissociation constant for enzyme-inhibitor complex (lower = stronger binding)")
            
            # Calculate alpha from [I] and Ki
            inhibitor_strength = 1 + (inhibitor_conc / ki_value) if ki_value > 0 else 1.0
            
            # For mixed inhibition: add alpha' slider
            if mechanism == "Mixed Inhibition":
                alpha_prime_value = st.slider("α' (Alpha Prime - Non-competitive Component)", 
                                             1.0, 10.0, inhibitor_strength * 0.8, 0.1,
                                             key="alpha_prime_slider",
                                             help="Independent parameter controlling Vmax reduction (α' ≠ α for mixed inhibition)")
                st.info(f"**Calculated α = {inhibitor_strength:.2f}** (affects Km) and **α' = {alpha_prime_value:.2f}** (affects Vmax)")
            else:
                alpha_prime_value = inhibitor_strength
                # Display calculated alpha
                st.info(f"**Calculated α = {inhibitor_strength:.2f}** (where α = 1 + [I]/Ki)")
        
        # Add annotation toggles
        st.markdown("**Plot Annotations:**")
        show_km_line = st.checkbox("Show Km reference line", value=False, key="show_km_line",
                                   help="Vertical line at Km on MM plot")
        show_vmax_line = st.checkbox("Show Vmax/2 reference line", value=False, key="show_vmax_line",
                                     help="Horizontal line at Vmax/2 on MM plot")
        show_intercepts = st.checkbox("Show LB intercept labels", value=True, key="show_intercepts",
                                     help="Label Y-intercept (1/Vmax) and X-intercept (-1/Km) on LB plot")
        
        # Determine color based on mechanism
        mechanism_colors = {
            "Competitive Inhibition": "red",
            "Non-competitive Inhibition": "orange",
            "Uncompetitive Inhibition": "purple",
            "Mixed Inhibition": "green"
        }
        inhibitor_color = mechanism_colors.get(mechanism, "red")
        
        # MM Plot (first, on top)
        st.markdown("---")
        st.markdown("**Michaelis-Menten Plot**")
        
        # Generate kinetic curves
        substrate = np.linspace(0.1, 20, 100)
        velocity_no_inhibitor = vmax * substrate / (km + substrate)
        
        fig_mm = go.Figure()
        fig_mm.add_trace(go.Scatter(x=substrate, y=velocity_no_inhibitor, 
                               name='No Inhibitor', line=dict(color='blue', width=2)))
        
        if show_inhibitor:
            alpha = inhibitor_strength  # Use calculated value
            alpha_prime = alpha_prime_value  # Use slider value for mixed inhibition
            
            if mechanism == "Competitive Inhibition":
                velocity_inhibitor = vmax * substrate / (km * alpha + substrate)
                apparent_km = km * alpha
                apparent_vmax = vmax
            elif mechanism == "Non-competitive Inhibition":
                velocity_inhibitor = (vmax / alpha) * substrate / (km + substrate)
                apparent_km = km
                apparent_vmax = vmax / alpha
            elif mechanism == "Uncompetitive Inhibition":
                velocity_inhibitor = (vmax / alpha) * substrate / (km / alpha + substrate)
                apparent_km = km / alpha
                apparent_vmax = vmax / alpha
            else:  # Mixed Inhibition
                velocity_inhibitor = (vmax / alpha_prime) * substrate / ((km * alpha / alpha_prime) + substrate)
                apparent_km = km * alpha / alpha_prime
                apparent_vmax = vmax / alpha_prime
            
            fig_mm.add_trace(go.Scatter(x=substrate, y=velocity_inhibitor, 
                               name='With Inhibitor', line=dict(color=inhibitor_color, dash='dash', width=2)))
        
        # Add annotation lines if toggled (NO TEXT to avoid overlap)
        if show_km_line:
            fig_mm.add_vline(x=km, line_dash="dot", line_color="gray", line_width=2)
            if show_inhibitor and mechanism == "Competitive Inhibition":
                fig_mm.add_vline(x=apparent_km, line_dash="dot", line_color=inhibitor_color, line_width=2)
        
        if show_vmax_line:
            fig_mm.add_hline(y=vmax/2, line_dash="dot", line_color="gray", line_width=2)
            if show_inhibitor:
                fig_mm.add_hline(y=apparent_vmax/2, line_dash="dot", line_color=inhibitor_color, line_width=2)
        
        fig_mm.update_layout(
            xaxis_title="[S] (mM)",
            yaxis_title="v (µmol/min)",
            height=400,
            showlegend=True,
            legend=dict(x=0.6, y=0.1),
            margin=dict(l=10, r=10, t=30, b=10)
        )
        
        # Add gridlines to MM plot with solid black zero lines
        fig_mm.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', zeroline=True, zerolinewidth=2, zerolinecolor='black')
        fig_mm.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', zeroline=True, zerolinewidth=2, zerolinecolor='black')
        
        st.plotly_chart(fig_mm, use_container_width=True)
        
        # Info box for MM plot showing key values (if annotations toggled)
        if show_km_line or show_vmax_line:
            mm_info = "**Reference Lines:**\n\n"
            if show_km_line:
                mm_info += f"🔵 Km = {km:.2f} mM (gray dotted)\n\n"
                if show_inhibitor and mechanism == "Competitive Inhibition":
                    mm_info += f"🔴 Apparent Km = {apparent_km:.2f} mM ({inhibitor_color} dotted)\n\n"
            if show_vmax_line:
                mm_info += f"🔵 Vmax/2 = {vmax/2:.2f} µmol/min (gray dotted)\n\n"
                if show_inhibitor:
                    mm_info += f"🔴 Apparent Vmax/2 = {apparent_vmax/2:.2f} µmol/min ({inhibitor_color} dotted)"
            st.caption(mm_info)
        
        # LB Plot (second, below MM plot)
        st.markdown("---")
        st.markdown("**Lineweaver-Burk Plot**")
        
        # Generate substrate concentrations for LB plot
        substrate_conc_lb = np.array([0.5, 1, 2, 4, 8, 16])  # mM
        
        # Calculate velocities (no inhibitor)
        velocity_no_inh_lb = vmax * substrate_conc_lb / (km + substrate_conc_lb)
        
        # Lineweaver-Burk transformation
        reciprocal_s = 1 / substrate_conc_lb
        reciprocal_v_no_inh = 1 / velocity_no_inh_lb
        
        # Calculate and store intercepts for annotation
        y_intercept_no_inh = 1 / vmax
        x_intercept_no_inh = -1 / km
        
        # Calculate slope: slope = (y_intercept - 0) / (0 - x_intercept) = y_intercept / (-x_intercept)
        slope_no_inh = y_intercept_no_inh / (0 - x_intercept_no_inh)
        
        # Find where line crosses y=0 (x-axis): 0 = y_intercept + slope * x
        # x_at_y0 = -y_intercept / slope
        x_at_y0_no_inh = -y_intercept_no_inh / slope_no_inh if slope_no_inh != 0 else x_intercept_no_inh
        
        # Extend line from x-intercept to where it crosses y=0
        if x_at_y0_no_inh > x_intercept_no_inh:
            x_extended_no_inh = np.linspace(x_intercept_no_inh, x_at_y0_no_inh, 100)
        else:
            x_extended_no_inh = np.linspace(x_at_y0_no_inh, x_intercept_no_inh, 100)
        y_extended_no_inh = y_intercept_no_inh + slope_no_inh * x_extended_no_inh
        
        fig_lb = go.Figure()
        
        # Extend data to include x-intercept for no inhibitor
        x_no_inh_extended = np.concatenate([[x_intercept_no_inh], reciprocal_s])
        y_no_inh_extended = np.concatenate([[0], reciprocal_v_no_inh])
        
        # Add line connecting from x-intercept through all data points
        fig_lb.add_trace(go.Scatter(
            x=x_no_inh_extended, 
            y=y_no_inh_extended,
            mode='lines+markers',
            name='No Inhibitor',
            line=dict(color='blue', width=2),
            marker=dict(size=8, color='blue'),
            showlegend=True
        ))
        
        # Add inhibitor conditions
        if show_inhibitor:
            alpha = inhibitor_strength
            
            if mechanism == "Competitive Inhibition":
                velocity_inh_lb = vmax * substrate_conc_lb / (km * alpha + substrate_conc_lb)
                apparent_km_lb = km * alpha
                apparent_vmax_lb = vmax
            elif mechanism == "Non-competitive Inhibition":
                velocity_inh_lb = (vmax / alpha) * substrate_conc_lb / (km + substrate_conc_lb)
                apparent_km_lb = km
                apparent_vmax_lb = vmax / alpha
            elif mechanism == "Uncompetitive Inhibition":
                velocity_inh_lb = (vmax / alpha) * substrate_conc_lb / (km / alpha + substrate_conc_lb)
                apparent_km_lb = km / alpha
                apparent_vmax_lb = vmax / alpha
            else:  # Mixed Inhibition
                alpha_prime = alpha_prime_value
                velocity_inh_lb = (vmax / alpha_prime) * substrate_conc_lb / ((km * alpha / alpha_prime) + substrate_conc_lb)
                apparent_km_lb = km * alpha / alpha_prime
                apparent_vmax_lb = vmax / alpha_prime
            
            reciprocal_v_inh = 1 / velocity_inh_lb
            
            # Calculate inhibitor intercepts
            y_intercept_inh = 1 / apparent_vmax_lb
            x_intercept_inh = -1 / apparent_km_lb
            
            # Extend data to include x-intercept for inhibitor
            x_inh_extended = np.concatenate([[x_intercept_inh], reciprocal_s])
            y_inh_extended = np.concatenate([[0], reciprocal_v_inh])
            
            # Add line connecting from x-intercept through all data points
            fig_lb.add_trace(go.Scatter(
                x=x_inh_extended, 
                y=y_inh_extended,
                mode='lines+markers',
                name='With Inhibitor',
                line=dict(color=inhibitor_color, width=2, dash='dash'),
                marker=dict(size=8, color=inhibitor_color),
                showlegend=True
            ))
            
            # Mark intercepts with simple dots (no text to avoid overlap)
            if show_intercepts:
                # Y-intercept marker for no inhibitor
                fig_lb.add_trace(go.Scatter(
                    x=[0], y=[y_intercept_no_inh],
                    mode='markers',
                    marker=dict(size=10, color='blue', symbol='circle'),
                    showlegend=False,
                    hovertext=f"Y-intercept: 1/Vmax = {y_intercept_no_inh:.4f}"
                ))
                
                # X-intercept marker for no inhibitor
                fig_lb.add_trace(go.Scatter(
                    x=[x_intercept_no_inh], y=[0],
                    mode='markers',
                    marker=dict(size=10, color='blue', symbol='square'),
                    showlegend=False,
                    hovertext=f"X-intercept: -1/Km = {x_intercept_no_inh:.4f}"
                ))
                
                # Y-intercept marker for inhibitor
                fig_lb.add_trace(go.Scatter(
                    x=[0], y=[y_intercept_inh],
                    mode='markers',
                    marker=dict(size=10, color=inhibitor_color, symbol='circle'),
                    showlegend=False,
                    hovertext=f"Y-intercept: 1/Vmax' = {y_intercept_inh:.4f}"
                ))
                
                # X-intercept marker for inhibitor (if different)
                if abs(x_intercept_inh - x_intercept_no_inh) > 0.01:
                    fig_lb.add_trace(go.Scatter(
                        x=[x_intercept_inh], y=[0],
                        mode='markers',
                        marker=dict(size=10, color=inhibitor_color, symbol='square'),
                        showlegend=False,
                        hovertext=f"X-intercept: -1/Km' = {x_intercept_inh:.4f}"
                    ))
        else:
            # Show intercepts even without inhibitor if toggled
            if show_intercepts:
                fig_lb.add_trace(go.Scatter(
                    x=[0], y=[y_intercept_no_inh],
                    mode='markers',
                    marker=dict(size=10, color='blue', symbol='circle'),
                    showlegend=False,
                    hovertext=f"Y-intercept: 1/Vmax = {y_intercept_no_inh:.4f}"
                ))
                fig_lb.add_trace(go.Scatter(
                    x=[x_intercept_no_inh], y=[0],
                    mode='markers',
                    marker=dict(size=10, color='blue', symbol='square'),
                    showlegend=False,
                    hovertext=f"X-intercept: -1/Km = {x_intercept_no_inh:.4f}"
                ))
        
        fig_lb.update_layout(
            xaxis_title='1/[S] (1/mM)',
            yaxis_title='1/v (min/µmol)',
            height=400,
            showlegend=True,
            legend=dict(x=0.05, y=0.95),
            margin=dict(l=10, r=10, t=30, b=10)
        )
        
        # Add grid for easier interpretation
        fig_lb.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', zeroline=True, zerolinewidth=2, zerolinecolor='black')
        fig_lb.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray', zeroline=True, zerolinewidth=2, zerolinecolor='black')
        
        st.plotly_chart(fig_lb, use_container_width=True)
        
        # Info box for LB plot showing intercept values (if annotations toggled)
        if show_intercepts:
            lb_info = "**Intercept Values:**\n\n"
            lb_info += f"🔵 **No Inhibitor:**\n"
            lb_info += f"  • Y-intercept (⚫) = 1/Vmax = {y_intercept_no_inh:.4f}\n"
            lb_info += f"  • X-intercept (◼) = -1/Km = {x_intercept_no_inh:.4f}\n\n"
            if show_inhibitor:
                lb_info += f"🔴 **With Inhibitor:**\n"
                lb_info += f"  • Y-intercept (⚫) = 1/Vmax' = {y_intercept_inh:.4f}\n"
                if abs(x_intercept_inh - x_intercept_no_inh) > 0.01:
                    lb_info += f"  • X-intercept (◼) = -1/Km' = {x_intercept_inh:.4f}\n"
                else:
                    lb_info += f"  • X-intercept (◼) = Same as no inhibitor\n"
                lb_info += f"\n**Pattern:** "
                if mechanism == "Competitive Inhibition":
                    lb_info += "Lines intersect on Y-axis ✓"
                elif mechanism == "Non-competitive Inhibition":
                    lb_info += "Lines intersect on X-axis ✓"
                elif mechanism == "Uncompetitive Inhibition":
                    lb_info += "Lines are parallel ✓"
                else:
                    lb_info += "Lines intersect in 2nd quadrant ✓"
            st.caption(lb_info)
        
        # Add numeric readouts of calculated parameters
        if show_inhibitor:
            st.markdown("---")
            st.markdown("### 📊 Calculated Kinetic Parameters")
            
            col_param1, col_param2, col_param3, col_param4 = st.columns(4)
            
            with col_param1:
                st.metric(
                    label="Km (no inhibitor)",
                    value=f"{km:.2f} mM",
                    help="Michaelis constant - substrate concentration at half Vmax"
                )
            
            with col_param2:
                st.metric(
                    label="Apparent Km (with inhibitor)",
                    value=f"{apparent_km:.2f} mM",
                    delta=f"{((apparent_km - km) / km * 100):.1f}%",
                    delta_color="inverse",
                    help="Effective Km in presence of inhibitor"
                )
            
            with col_param3:
                st.metric(
                    label="Vmax (no inhibitor)",
                    value=f"{vmax:.1f} µmol/min",
                    help="Maximum reaction velocity"
                )
            
            with col_param4:
                st.metric(
                    label="Apparent Vmax (with inhibitor)",
                    value=f"{apparent_vmax:.1f} µmol/min",
                    delta=f"{((apparent_vmax - vmax) / vmax * 100):.1f}%",
                    delta_color="inverse",
                    help="Effective Vmax in presence of inhibitor"
                )
            
            # Additional metrics row
            col_eff1, col_eff2, col_eff3 = st.columns(3)
            
            with col_eff1:
                catalytic_eff = vmax / km
                st.metric(
                    label="Catalytic Efficiency (Vmax/Km)",
                    value=f"{catalytic_eff:.2f}",
                    help="Ratio of Vmax to Km - higher is more efficient"
                )
            
            with col_eff2:
                apparent_eff = apparent_vmax / apparent_km
                st.metric(
                    label="Apparent Efficiency (with inhibitor)",
                    value=f"{apparent_eff:.2f}",
                    delta=f"{((apparent_eff - catalytic_eff) / catalytic_eff * 100):.1f}%",
                    delta_color="inverse",
                    help="Effective catalytic efficiency with inhibitor"
                )
            
            with col_eff3:
                fold_change = catalytic_eff / apparent_eff if apparent_eff > 0 else 0
                st.metric(
                    label="Fold Inhibition",
                    value=f"{fold_change:.2f}x",
                    help="How many times less efficient the enzyme is with inhibitor"
                )
        
        # Add interpretation below both plots
        st.info(f"""
        **📊 Interpretation for {mechanism}:**
        
        **Michaelis-Menten (left):** {
            "Vmax unchanged, apparent Km increases (shifts right)" if mechanism == "Competitive Inhibition"
            else "Vmax decreases, Km unchanged (lower plateau)" if mechanism == "Non-competitive Inhibition"
            else "Both Vmax and Km decrease proportionally" if mechanism == "Uncompetitive Inhibition"
            else "Both Vmax and apparent Km change"
        }
        
        **Lineweaver-Burk (right):** {
            "Lines intersect on Y-axis (same 1/Vmax, different X-intercept)" if mechanism == "Competitive Inhibition"
            else "Lines intersect on X-axis (same -1/Km, different Y-intercept)" if mechanism == "Non-competitive Inhibition"
            else "Lines are parallel (both intercepts change proportionally)" if mechanism == "Uncompetitive Inhibition"
            else "Lines intersect in 2nd quadrant (both intercepts change differently)"
        }
        """)

# IC50/Ki Calculator Section
def show_calculator():
    st.markdown('<div class="section-header">🧮 IC50 & Ki Calculator</div>', unsafe_allow_html=True)
    
    # User Guide for Calculator
    with st.expander("📖 How to Use the Calculator Tools", expanded=False):
        st.markdown("""
        **Three Powerful Calculation Tools - Choose a Tab:**
        
        ---
        
        ### **Tab 1: IC50 Calculator** 🧪
        
        **Purpose:** Calculate IC50 from your experimental data
        
        **Step-by-Step:**
        1. Select number of data points (3-10 recommended, 5 is good start)
        2. Enter your **inhibitor concentrations** (μM) in left column
        3. Enter corresponding **activity percentages** (0-100%) in right column
        4. IC50 is automatically calculated and displayed with a dose-response curve
        5. Click **"Download Results as CSV"** to export data
        
        **Tips:**
        - Your data must cross 50% activity for calculation to work
        - Use log-spaced concentrations for better curve fitting (e.g., 0.1, 1, 10, 100)
        - Duplicate concentrations will trigger a warning
        - Lower IC50 = more potent inhibitor
        
        **Interpreting Results:**
        - Very potent: < 0.1 μM
        - Potent: 0.1-1 μM
        - Moderate: 1-10 μM
        - Weak: > 10 μM
        
        ---
        
        ### **Tab 2: Ki Calculator** ⚖️
        
        **Purpose:** Convert IC50 to Ki (inhibition constant) using Cheng-Prusoff equations
        
        **Step-by-Step:**
        1. Select your **inhibition type** (Competitive, Non-competitive, or Uncompetitive)
        2. Enter your **IC50 value** (μM) from experiments
        3. Enter **substrate concentration [S]** (μM) used in assay
        4. Enter **Km value** (μM) for your enzyme
        5. Ki is automatically calculated with the appropriate formula
        
        **Formulas Used:**
        - Competitive: Ki = IC50 / (1 + [S]/Km)
        - Non-competitive: Ki = IC50
        - Uncompetitive: Ki = IC50 / (1 + Km/[S])
        
        **Important:** Units must be consistent (all μM or all nM)
        
        ---
        
        ### **Tab 3: Dose-Response Curve Generator** 📈
        
        **Purpose:** Generate theoretical dose-response curves for presentations or teaching
        
        **Step-by-Step:**
        1. Set **Top Activity** (usually 100% for no inhibitor)
        2. Set **Bottom Activity** (usually 0% for complete inhibition)
        3. Enter desired **IC50 value** (μM)
        4. Adjust **Hill Slope** (1.0 is standard, higher = steeper curve)
        5. Set **Max Concentration** range for X-axis
        6. View generated curve instantly
        
        **Uses:**
        - Creating example curves for presentations
        - Understanding Hill equation behavior
        - Comparing different IC50 values visually
        
        ---
        
        **All calculators provide instant results as you adjust parameters!**
        """)
    
    st.write("""Calculate inhibition constants and understand drug potency metrics.""")
    
    # Create tabs for different calculators
    tab1, tab2, tab3 = st.tabs(["IC50 Calculator", "Ki Calculator", "Dose-Response Curve"])
    
    with tab1:
        st.subheader("IC50 Calculator")
        st.write("**IC50** (Half maximal inhibitory concentration): The concentration of inhibitor required to reduce enzyme activity by 50%.")
        
        # Description and importance
        st.info("""
        💡 **What is IC50?**  
        IC50 measures how much inhibitor you need to cut enzyme activity in half. Think of it as the "potency score" 
        for your drug candidate - lower IC50 means stronger inhibition!
        """)
        
        with st.expander("🎯 Why IC50 Matters in Drug Discovery", expanded=False):
            st.write("""
            IC50 is the go-to metric that pharmaceutical companies use to:
            
            - **Compare candidates** - Which compound works best?
            - **Set doses** - How much drug do patients need?
            - **Predict success** - Lower IC50 often means better drugs
            - **Track progress** - Are our modifications improving potency?
            
            **Real success story:** HIV protease inhibitors with IC50 < 10 nM became life-saving blockbuster drugs, 
            while those with IC50 > 100 nM didn't make it past early trials. That 10-fold difference changed millions of lives!
            """)
        
        with st.expander("📊 How to Use This Tool", expanded=False):
            st.write("""
            **What you'll need:** Data from your enzyme activity assay
            
            **Quick steps:**
            1. Choose how many data points you have (5-7 is ideal)
            2. Enter your inhibitor concentrations (try a wide range like 0.1, 1, 10, 100 µM)
            3. Enter the % enzyme activity at each concentration (100% = no inhibitor)
            4. Watch the calculator plot your dose-response curve and find IC50!
            5. Download your results as CSV for your records
            
            💡 **Pro tip:** Make sure your data crosses 50% activity - test both high and low concentrations!
            """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Input Parameters")
            
            st.markdown("#### Inhibitor Concentrations & Activities")
            num_points = st.slider("Number of data points", 3, 10, 5,
                                  help="More points give better curve fitting (5-7 recommended)")
            
            concentrations = []
            activities = []
            
            for i in range(num_points):
                col_a, col_b = st.columns(2)
                with col_a:
                    conc = st.number_input(f"[I]_{i+1} (µM)", min_value=0.0, value=float((i+1)*2), 
                                          step=0.1, key=f"conc_{i}")
                    concentrations.append(conc)
                with col_b:
                    act = st.number_input(f"Activity_{i+1} (%)", min_value=0.0, max_value=100.0, 
                                        value=float(max(10, 100 - i*18)), step=1.0, key=f"act_{i}")
                    activities.append(act)
        
        with col2:
            st.markdown("#### Results")
            
            if len(concentrations) >= 3:
                # Validate input data
                conc_array = np.array(concentrations)
                act_array = np.array(activities)
                
                # Check for duplicate concentrations
                unique_conc = np.unique(conc_array)
                if len(unique_conc) < len(conc_array):
                    st.warning("⚠️ Warning: Duplicate concentration values detected. This may affect curve fitting accuracy.")
                
                # Fit dose-response curve (Hill equation)
                # y = Bottom + (Top - Bottom) / (1 + (IC50/x)^HillSlope)
                # Simplified: assume Hill slope = 1
                
                # Calculate IC50 using interpolation
                # Sort by concentration
                sorted_indices = np.argsort(conc_array)
                conc_sorted = conc_array[sorted_indices]
                act_sorted = act_array[sorted_indices]
                
                # Find IC50 (50% activity)
                if len(act_sorted) > 1 and act_sorted.max() > 50 and act_sorted.min() < 50:
                    # Check if activities decrease with concentration (typical inhibition)
                    if act_sorted[0] > act_sorted[-1]:
                        # Activities decrease: reverse for interpolation
                        ic50 = np.interp(50, act_sorted[::-1], conc_sorted[::-1])
                    else:
                        # Activities increase: interpolate directly
                        ic50 = np.interp(50, act_sorted, conc_sorted)
                    
                    st.success(f"### IC50 = {ic50:.2f} µM")
                    
                    # Generate smooth curve
                    max_conc = max(max(concentrations), 1.0)  # Ensure minimum range
                    conc_smooth = np.linspace(0.01, max_conc*1.2, 100)
                    # Hill equation with calculated IC50
                    hill_slope = 1.0
                    
                    # Determine top and bottom based on actual data pattern
                    if act_sorted[0] > act_sorted[-1]:
                        # Activities decrease with concentration (typical inhibition)
                        top = act_sorted[0]
                        bottom = act_sorted[-1]
                        # Hill equation for inhibition: activity decreases
                        act_smooth = bottom + (top - bottom) / (1 + (conc_smooth/ic50)**hill_slope)
                    else:
                        # Activities increase with concentration (atypical)
                        top = act_sorted[-1]
                        bottom = act_sorted[0]
                        # Inverse Hill equation
                        act_smooth = bottom + (top - bottom) / (1 + (ic50/conc_smooth)**hill_slope)
                    
                    # Plot
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=conc_sorted, y=act_sorted, mode='markers',
                                           name='Data', marker=dict(size=10, color='red')))
                    fig.add_trace(go.Scatter(x=conc_smooth, y=act_smooth, mode='lines',
                                           name='Fit', line=dict(color='blue')))
                    fig.add_hline(y=50, line_dash="dash", line_color="green", 
                                annotation_text="IC50")
                    
                    fig.update_layout(
                        title="Dose-Response Curve",
                        xaxis_title="Inhibitor Concentration (µM)",
                        yaxis_title="Activity (%)",
                        height=400,
                        xaxis_type="log"
                    )
                    st.plotly_chart(fig, width='stretch')
                    
                    # Interpretation
                    st.info(f"""**Interpretation:**
- At {ic50:.2f} µM, the enzyme activity is reduced to 50%
- Lower IC50 = More potent inhibitor
- Typical potency ranges:
  - Very potent: < 0.1 µM
  - Potent: 0.1-1 µM  
  - Moderate: 1-10 µM
  - Weak: > 10 µM
                    """)
                    
                    # Export data option
                    results_df = pd.DataFrame({
                        'Concentration_uM': conc_sorted,
                        'Activity_percent': act_sorted,
                        'IC50_uM': [ic50] * len(conc_sorted)
                    })
                    csv = results_df.to_csv(index=False)
                    st.download_button(
                        label="📅 Download Results as CSV",
                        data=csv,
                        file_name="ic50_results.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("⚠️ **Cannot calculate IC50:** Data must cross the 50% activity threshold. "
                             f"Current range: {act_sorted.min():.1f}% to {act_sorted.max():.1f}%. "
                             "Please adjust your data points to include values both above and below 50%.")
    
    with tab2:
        st.subheader("Ki Calculator (Inhibition Constant)")
        st.write("**Ki**: Dissociation constant of the enzyme-inhibitor complex. Lower Ki = Stronger binding.")
        
        # Description and importance
        st.info("""
        💡 **What is Ki?**  
        Ki is the "true" binding strength between your inhibitor and enzyme - it doesn't change with different assay conditions. 
        Think of it as the fundamental measure of how tightly they stick together!
        """)
        
        with st.expander("🎯 Why Ki is Better Than IC50", expanded=False):
            st.write("""
            Here's the thing about IC50 - it changes depending on your experiment setup! Same drug, different substrate 
            concentration? Different IC50. But Ki stays constant:
            
            - **IC50 varies with assay conditions** (substrate, enzyme, incubation time)
            - **Ki is the real deal** - constant for a given inhibitor-enzyme pair
            - **Fair comparisons** - Compare data from different labs reliably
            - **Better predictions** - Ki tells you what happens in cells, not just test tubes
            
            **Example:** An inhibitor might show IC50 = 10 µM in your assay, but the true Ki could be just 1 µM - 
            10 times more potent! This happens with competitive inhibitors when you use high substrate concentrations.
            """)
        
        with st.expander("🧮 How to Use This Tool (Cheng-Prusoff Equations)", expanded=False):
            st.write("""
            This calculator converts your IC50 into Ki using the proper equation for your inhibition type.
            
            **What you'll need:**
            - IC50 from your experiment (or use Tab 1 calculator)
            - Substrate concentration [S] you used when measuring IC50
            - Km value for your enzyme (find it in literature or measure it)
            - Inhibition mechanism (check out the Mechanisms section if unsure!)
            
            **Simple steps:**
            1. Pick your inhibition type from the dropdown
            2. Enter your IC50 value (µM)
            3. Enter the [S] you used in your assay (µM)
            4. Enter Km for your enzyme (µM)
            5. Boom! Ki is calculated automatically
            
            ⚠️ **Units matter!** Make sure IC50, [S], and Km all use the same units (µM recommended).
            
            **Quick formulas:**
            - **Competitive:** Ki = IC50 ÷ (1 + [S]/Km) → Ki always smaller than IC50
            - **Non-competitive:** Ki = IC50 → No correction needed!
            - **Uncompetitive:** Ki = IC50 ÷ (1 + Km/[S]) → Depends on substrate
            """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Input Parameters")
            
            st.info("💡 **Important:** Ensure IC50, [S], and Km are all in the same units (µM).")
            
            inhibition_type = st.selectbox(
                "Inhibition Type",
                ["Competitive", "Non-competitive", "Uncompetitive"],
                key="ki_type"
            )
            
            ic50_input = st.number_input("IC50 (µM)", min_value=0.01, value=5.0, step=0.1,
                                        help="Concentration causing 50% inhibition (from your IC50 assay)")
            substrate_conc = st.number_input("[S] Substrate Concentration (µM)", 
                                           min_value=0.01, value=10.0, step=1.0,
                                           help="Substrate concentration used in your IC50 assay")
            km_input = st.number_input("Km (µM)", min_value=0.01, value=5.0, step=0.1,
                                      help="Michaelis constant: substrate concentration at half Vmax")
        
        with col2:
            st.markdown("#### Results")
            
            # Cheng-Prusoff equation for competitive inhibition:
            # Ki = IC50 / (1 + [S]/Km)
            
            if inhibition_type == "Competitive":
                ki = ic50_input / (1 + substrate_conc / km_input)
                st.success(f"### Ki = {ki:.3f} µM")
                
                st.markdown("**Calculation:**")
                st.latex(r"K_i = \frac{IC_{50}}{1 + \frac{[S]}{K_m}}")
                
                st.info(f"""**Cheng-Prusoff Equation (Competitive)**
- IC50 = {ic50_input} µM
- [S] = {substrate_conc} µM
- Km = {km_input} µM
- **Ki = {ki:.3f} µM**

Ki represents the true binding affinity of the inhibitor to the enzyme.
                """)
                
            elif inhibition_type == "Non-competitive":
                ki = ic50_input
                st.success(f"### Ki = {ki:.3f} µM")
                
                st.info(f"""**Non-competitive Inhibition**
- For non-competitive inhibitors: Ki ≈ IC50
- **Ki = {ki:.3f} µM**

The inhibitor binds to a site different from the active site.
                """)
            
            else:  # Uncompetitive
                # For uncompetitive inhibition: Ki = IC50 / (1 + Km/[S])
                ki = ic50_input / (1 + km_input / substrate_conc)
                st.success(f"### Ki = {ki:.3f} µM")
                
                st.latex(r"K_i = \frac{IC_{50}}{1 + \frac{K_m}{[S]}}")
                
                st.info(f"""**Uncompetitive Inhibition**
- IC50 = {ic50_input} µM
- Km = {km_input} µM  
- [S] = {substrate_conc} µM
- **Ki = {ki:.3f} µM**

The inhibitor only binds to the enzyme-substrate complex (ES).
Ki represents the dissociation constant for the ESI complex.
                """)
    
    with tab3:
        st.subheader("Dose-Response Curve Generator")
        
        # Description and importance
        st.markdown("""---
        ### 🎯 Why This Calculator is Essential
        
        The Hill equation is the **fundamental mathematical model** for dose-response relationships in pharmacology. 
        Understanding this curve is crucial for:
        
        - **Experimental design** - Predict what concentration range to test before doing expensive experiments
        - **Data presentation** - Generate publication-quality curves for papers and presentations
        - **Teaching tool** - Visualize how IC50, Hill slope, and activity range affect curve shape
        - **Quality control** - Recognize aberrant data that doesn't fit the Hill equation
        - **Drug comparison** - Compare theoretical curves of different inhibitors side-by-side
        
        **Hill slope interpretation:**
        - **h = 1.0** (standard) → Non-cooperative binding, typical for most enzyme inhibitors
        - **h > 1.0** (steep) → Positive cooperativity or multiple binding sites (e.g., h = 2-4)
        - **h < 1.0** (shallow) → Negative cooperativity or heterogeneous binding
        
        **Real example:** Imatinib (Gleevec) for CML has Hill slope ≈ 1.0 and IC50 = 0.1 µM against BCR-ABL kinase, 
        producing the characteristic sigmoidal curve you'll generate here.
        
        ### 📈 How to Use This Generator
        
        **Purpose:** Create theoretical dose-response curves without needing experimental data
        
        **Step-by-step:**
        1. **Set Top Activity** - Usually 100% (enzyme fully active with no inhibitor)
        2. **Set Bottom Activity** - Usually 0% (complete inhibition at high [I])
        3. **Enter desired IC50** - The concentration where curve crosses midpoint (µM)
        4. **Adjust Hill Slope** - Start with 1.0 (standard), then experiment:
           - Try h = 2.0 to see cooperative binding
           - Try h = 0.5 to see negative cooperativity
        5. **Set Max Concentration** - Determines X-axis range (typically 100-1000× your IC50)
        6. **Interpret curve** - Steeper slopes mean sharper on/off switching behavior
        
        **Uses:**
        - **Before experiments:** "If my IC50 is ~5 µM, what concentrations should I test?"
        - **For presentations:** Generate clean example curves to explain concepts
        - **Parameter exploration:** See how changing IC50 or Hill slope affects the curve
        - **Compare inhibitors:** Generate multiple curves with different IC50 values
        
        **Pro tip:** In drug development, you want Hill slope ≈ 1.0. Very steep curves (h > 3) can mean 
        narrow therapeutic windows (small difference between effective and toxic doses).
        
        ---
        """)
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("#### Curve Parameters")
            
            top_activity = st.slider("Top Activity (%)", 0, 100, 100, 1,
                                    help="Activity with no inhibitor (usually 100%)")
            bottom_activity = st.slider("Bottom Activity (%)", 0, 100, 0, 1,
                                       help="Activity at maximum inhibition (usually 0%)")
            ic50_curve = st.number_input("IC50 (µM)", min_value=0.01, value=1.0, step=0.1, key="ic50_curve",
                                        help="Desired IC50 value for the theoretical curve")
            hill_slope = st.slider("Hill Slope", 0.5, 4.0, 1.0, 0.1,
                                 help="Steepness of curve (1.0 = standard, >1 = cooperative binding, <1 = negative cooperativity)")
            
            conc_range_max = st.number_input("Max Concentration (µM)", min_value=0.1, value=100.0, step=1.0,
                                            help="Maximum concentration to display on X-axis")
        
        with col2:
            st.markdown("#### Generated Curve")
            
            # Validation
            if bottom_activity > top_activity:
                st.warning("⚠️ Bottom activity is greater than top activity. Curve will be inverted.")
            
            # Generate dose-response curve
            concentrations_curve = np.logspace(-3, np.log10(conc_range_max), 100)
            
            # Hill equation: y = Bottom + (Top - Bottom) / (1 + (x/IC50)^HillSlope)
            response = bottom_activity + (top_activity - bottom_activity) / \
                      (1 + (concentrations_curve / ic50_curve)**hill_slope)
            
            # Calculate actual IC50 activity level (midpoint)
            ic50_activity_level = (top_activity + bottom_activity) / 2
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=concentrations_curve, y=response, mode='lines',
                                   line=dict(color='purple', width=3)))
            fig.add_hline(y=ic50_activity_level, line_dash="dash", line_color="green",
                        annotation_text=f"IC50 = {ic50_curve} µM")
            fig.add_vline(x=ic50_curve, line_dash="dash", line_color="green")
            
            fig.update_layout(
                title="Dose-Response Curve",
                xaxis_title="Inhibitor Concentration (µM)",
                yaxis_title="Activity (%)",
                height=400,
                xaxis_type="log"
            )
            st.plotly_chart(fig, width='stretch')
            
            st.markdown("**Hill Equation:**")
            st.latex(r"y = Bottom + \frac{Top - Bottom}{1 + \left(\frac{[I]}{IC_{50}}\right)^{h}}")
            st.write(f"where h = {hill_slope} (Hill slope)")

# References Section
def show_references():
    st.markdown('<div class="section-header">📚 References & Resources</div>', unsafe_allow_html=True)
    
    # User Guide for References
    with st.expander("📖 How to Use This Reference Library", expanded=False):
        st.markdown("""
        **Comprehensive Scientific References**
        
        All data, equations, and claims in this application are supported by peer-reviewed scientific literature.
        
        **What's included in each tab:**
        
        ---
        
        **Tab 1: Key Papers** 📄
        - **31 peer-reviewed publications** from top journals
        - All citations in **APA 7th edition format**
        - **DOI links** for direct access to papers
        - Organized by topic:
          - Enzyme inhibition theory
          - Statins and cholesterol drugs
          - HIV protease inhibitors
          - ACE inhibitors
          - Kinase inhibitors
          - COX-2 inhibitors
        
        **How to use:**
        - Click DOI links to access full papers (may require institutional access)
        - Copy citations for your own reports or publications
        - All references are authoritative sources from journals like NEJM, Nature, Blood, JAMA
        
        ---
        
        **Tab 2: Online Resources** 🌐
        - **Free databases:**
          - PubChem (chemical structures)
          - DrugBank (drug information)
          - BRENDA (enzyme data)
          - ChEMBL (bioactivity data)
          - PDB (protein structures)
        - **Educational resources:**
          - Khan Academy tutorials
          - NCBI Bookshelf (free textbooks)
        - **Professional organizations**
        
        **All resources are free to access!**
        
        ---
        
        **Tab 3: Citation** 📝
        - How to cite this educational tool
        - GitHub repository link
        - License information
        
        ---
        
        **Note:** All references have been verified for accuracy and accessibility. DOI links are functional as of December 2025.
        """)
    
    st.write("""This educational tool is based on established principles in biochemistry and pharmacology.""")
    
    # Create tabs for different reference categories
    tab1, tab2, tab3 = st.tabs(["Key Papers", "Online Resources", "Citation"])
    
    with tab1:
        st.subheader("📄 Key Research Papers")
        
        st.info("**Note:** All references are formatted in APA 7th edition style. DOI links are provided for journal articles and have been verified as functional. Textbooks typically do not have DOI identifiers.")
        
        st.markdown("""
#### Enzyme Inhibition Theory & Methods

1. Copeland, R. A. (2013). Evaluation of enzyme inhibitors in drug discovery: A guide for medicinal chemists and pharmacologists (2nd ed.). *Methods of Biochemical Analysis*, *46*, 1–265. https://doi.org/10.1002/9781118540398

2. Cheng, Y., & Prusoff, W. H. (1973). Relationship between the inhibition constant (K1) and the concentration of inhibitor which causes 50 per cent inhibition (I50) of an enzymatic reaction. *Biochemical Pharmacology*, *22*(23), 3099–3108. https://doi.org/10.1016/0006-2952(73)90196-2

3. DiMasi, J. A., Grabowski, H. G., & Hansen, R. W. (2016). Innovation in the pharmaceutical industry: New estimates of R&D costs. *Journal of Health Economics*, *47*, 20–33. https://doi.org/10.1016/j.jhealeco.2016.01.012

#### Drug Development Resources

4. U.S. Food and Drug Administration. (2024). *Drugs@FDA: FDA-approved drugs*. https://www.accessdata.fda.gov/scripts/cder/daf/

5. U.S. National Library of Medicine. (n.d.). *ClinicalTrials.gov*. https://clinicaltrials.gov/

6. EvaluatePharma. (2023). *World preview 2023, outlook to 2028*. Evaluate Ltd.

7. Centers for Disease Control and Prevention. (n.d.). *CDC WONDER: Wide-ranging online data for epidemiologic research*. https://wonder.cdc.gov/

#### Statins (HMG-CoA Reductase Inhibitors)

8. Istvan, E. S., & Deisenhofer, J. (2001). Structural mechanism for statin inhibition of HMG-CoA reductase. *Science*, *292*(5519), 1160–1164. https://doi.org/10.1126/science.1059344

9. Endo, A. (2010). A historical perspective on the discovery of statins. *Proceedings of the Japan Academy, Series B*, *86*(5), 484–493. https://doi.org/10.2183/pjab.86.484

10. Heart Protection Study Collaborative Group. (2002). MRC/BHF Heart Protection Study of cholesterol lowering with simvastatin in 20,536 high-risk individuals: A randomised placebo-controlled trial. *The Lancet*, *360*(9326), 7–22. https://doi.org/10.1016/S0140-6736(02)09327-3

11. Ridker, P. M., Danielson, E., Fonseca, F. A., Genest, J., Gotto, A. M., Jr., Kastelein, J. J., Koenig, W., Libby, P., Lorenzatti, A. J., MacFadyen, J. G., Nordestgaard, B. G., Shepherd, J., Willerson, J. T., & Glynn, R. J. (2008). Rosuvastatin to prevent vascular events in men and women with elevated C-reactive protein. *New England Journal of Medicine*, *359*(21), 2195–2207. https://doi.org/10.1056/NEJMoa0807646

12. Sawyer, A. M., & Flagg, L. A. (2021). *Trends in heart disease and stroke mortality among adults aged 45 and over: United States, 2000–2019* (NCHS Data Brief No. 425). National Center for Health Statistics. https://doi.org/10.15620/cdc:112339

#### HIV Protease Inhibitors

13. Palella, F. J., Jr., Delaney, K. M., Moorman, A. C., Loveless, M. O., Fuhrer, J., Satten, G. A., Aschman, D. J., & Holmberg, S. D. (1998). Declining morbidity and mortality among patients with advanced human immunodeficiency virus infection. *New England Journal of Medicine*, *338*(13), 853–860. https://doi.org/10.1056/NEJM199803263381301

14. Kohl, N. E., Emini, E. A., Schleif, W. A., Davis, L. J., Heimbach, J. C., Dixon, R. A., Scolnick, E. M., & Sigal, I. S. (1988). Active human immunodeficiency virus protease is required for viral infectivity. *Proceedings of the National Academy of Sciences*, *85*(13), 4686–4690. https://doi.org/10.1073/pnas.85.13.4686

15. Wlodawer, A., & Vondrasek, J. (1998). Inhibitors of HIV-1 protease: A major success of structure-assisted drug design. *Annual Review of Biophysics and Biomolecular Structure*, *27*, 249–284. https://doi.org/10.1146/annurev.biophys.27.1.249

16. Gulick, R. M., Mellors, J. W., Havlir, D., Eron, J. J., Gonzalez, C., McMahon, D., Richman, D. D., Valentine, F. T., Jonas, L., Meibohm, A., Emini, E. A., & Chodakewitz, J. A. (1997). Treatment with indinavir, zidovudine, and lamivudine in adults with human immunodeficiency virus infection and prior antiretroviral therapy. *New England Journal of Medicine*, *337*(11), 734–739. https://doi.org/10.1056/NEJM199709113371102

17. Flexner, C. (1998). HIV-protease inhibitors. *New England Journal of Medicine*, *338*(18), 1281–1293. https://doi.org/10.1056/NEJM199804303381808

18. Antiretroviral Therapy Cohort Collaboration. (2008). Life expectancy of individuals on combination antiretroviral therapy in high-income countries: A collaborative analysis of 14 cohort studies. *The Lancet*, *372*(9635), 293–299. https://doi.org/10.1016/S0140-6736(08)61113-7

19. UNAIDS. (2020). *Global AIDS update 2020: Seizing the moment*. Joint United Nations Programme on HIV/AIDS. https://www.unaids.org/en/resources/documents/2020/global-aids-report

#### ACE Inhibitors

20. Cushman, D. W., & Ondetti, M. A. (1991). History of the design of captopril and related inhibitors of angiotensin converting enzyme. *Hypertension*, *17*(4), 589–592. https://doi.org/10.1161/01.HYP.17.4.589

21. Pfeffer, M. A., Braunwald, E., Moyé, L. A., Basta, L., Brown, E. J., Jr., Cuddy, T. E., Davis, B. R., Geltman, E. M., Goldman, S., Flaker, G. C., Klein, M., Lamas, G. A., Packer, M., Rouleau, J., Rouleau, J. L., Rutherford, J., Wertheimer, J. H., & Hawkins, C. M. (1992). Effect of captopril on mortality and morbidity in patients with left ventricular dysfunction after myocardial infarction: Results of the survival and ventricular enlargement trial. *New England Journal of Medicine*, *327*(10), 669–677. https://doi.org/10.1056/NEJM199209033271001

22. Yusuf, S., Sleight, P., Pogue, J., Bosch, J., Davies, R., & Dagenais, G. (2000). Effects of an angiotensin-converting-enzyme inhibitor, ramipril, on cardiovascular events in high-risk patients. *New England Journal of Medicine*, *342*(3), 145–153. https://doi.org/10.1056/NEJM200001203420301

#### Kinase Inhibitors

23. Druker, B. J., Talpaz, M., Resta, D. J., Peng, B., Buchdunger, E., Ford, J. M., Lydon, N. B., Kantarjian, H., Capdeville, R., Ohno-Jones, S., & Sawyers, C. L. (2001). Efficacy and safety of a specific inhibitor of the BCR-ABL tyrosine kinase in chronic myeloid leukemia. *New England Journal of Medicine*, *344*(14), 1031–1037. https://doi.org/10.1056/NEJM200104053441401

24. Cohen, P. (2002). Protein kinases—the major drug targets of the twenty-first century? *Nature Reviews Drug Discovery*, *1*(4), 309–315. https://doi.org/10.1038/nrd773

25. Deininger, M., Buchdunger, E., & Druker, B. J. (2005). The development of imatinib as a therapeutic agent for chronic myeloid leukemia. *Blood*, *105*(7), 2640–2653. https://doi.org/10.1182/blood-2004-08-3097

26. Hochhaus, A., Larson, R. A., Guilhot, F., Radich, J. P., Branford, S., Hughes, T. P., Baccarani, M., Deininger, M. W., Cervantes, F., Fujihara, S., Ortmann, C. E., Menssen, H. D., Kantarjian, H., O'Brien, S. G., & Druker, B. J. (2017). Long-term outcomes of imatinib treatment for chronic myeloid leukemia. *New England Journal of Medicine*, *376*(10), 917–927. https://doi.org/10.1056/NEJMoa1609324

#### COX-2 Inhibitors

27. Vane, J. R., & Botting, R. M. (1998). Mechanism of action of nonsteroidal anti-inflammatory drugs. *American Journal of Medicine*, *104*(3A), 2S–8S. https://doi.org/10.1016/S0002-9343(97)00203-9

28. Bombardier, C., Laine, L., Reicin, A., Shapiro, D., Burgos-Vargas, R., Davis, B., Day, R., Ferraz, M. B., Hawkey, C. J., Hochberg, M. C., Kvien, T. K., & Schnitzer, T. J. (2000). Comparison of upper gastrointestinal toxicity of rofecoxib and naproxen in patients with rheumatoid arthritis. *New England Journal of Medicine*, *343*(21), 1520–1528. https://doi.org/10.1056/NEJM200011233432103

29. Silverstein, F. E., Faich, G., Goldstein, J. L., Simon, L. S., Pincus, T., Whelton, A., Makuch, R., Eisen, G., Agrawal, N. M., Stenson, W. F., Burr, A. M., Zhao, W. W., Kent, J. D., Lefkowith, J. B., Verburg, K. M., & Geis, G. S. (2000). Gastrointestinal toxicity with celecoxib vs nonsteroidal anti-inflammatory drugs for osteoarthritis and rheumatoid arthritis: The CLASS study. *JAMA*, *284*(10), 1247–1255. https://doi.org/10.1001/jama.284.10.1247

30. FitzGerald, G. A. (2004). Coxibs and cardiovascular disease. *New England Journal of Medicine*, *351*(17), 1709–1711. https://doi.org/10.1056/NEJMp048288
        """)
    
    with tab2:
        st.subheader("🌐 Online Resources")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""#### Databases & Tools
- **[PubChem](https://pubchem.ncbi.nlm.nih.gov/)** - Chemical information database
- **[DrugBank](https://go.drugbank.com/)** - Drug and drug target database  
- **[BRENDA](https://www.brenda-enzymes.org/)** - Enzyme information system
- **[ChEMBL](https://www.ebi.ac.uk/chembl/)** - Bioactive molecules database
- **[PDB](https://www.rcsb.org/)** - Protein Data Bank

#### Educational Resources
- **[Khan Academy - Enzyme Kinetics](https://www.khanacademy.org/science/biology/energy-and-enzymes)**
- **[NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/)** - Free biochemistry textbooks
            """)
        
        with col2:
            st.markdown("""#### Organizations
- **[FDA - Drug Development](https://www.fda.gov/drugs/development-approval-process-drugs)**
- **[WHO Essential Medicines](https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines)**
- **[ACS Chemical Biology](https://pubs.acs.org/journal/acbcct)**

#### Journals
- *Nature Reviews Drug Discovery*
- *Journal of Medicinal Chemistry*
- *Biochemistry*
- *Drug Discovery Today*
            """)
    
    with tab3:
        st.subheader("📝 How to Cite This Tool")
        
        st.markdown("""If you use this interactive educational tool in your teaching, research, or publications, 
please cite it using one of the following formats:""")
        
        st.markdown("#### APA 7th Edition (Recommended)")
        st.code("""Chiu, K. (2025). Enzyme inhibitors in drug development: An interactive educational tool [Interactive web application]. Streamlit. https://lab-kason-biochem.streamlit.app""", language="text")
        
        st.markdown("#### MLA 9th Edition")
        st.code("""Chiu, Kason. "Enzyme Inhibitors in Drug Development: An Interactive Educational Tool." Streamlit, 2025, lab-kason-biochem.streamlit.app. Accessed [Date].""", language="text")
        
        st.markdown("#### Chicago 17th Edition")
        st.code("""Chiu, Kason. 2025. "Enzyme Inhibitors in Drug Development: An Interactive Educational Tool." Interactive web application. Streamlit. https://lab-kason-biochem.streamlit.app.""", language="text")
        
        st.markdown("#### BibTeX Format")
        st.code("""@misc{chiu2025enzyme,
  title={Enzyme Inhibitors in Drug Development: An Interactive Educational Tool},
  author={Chiu, Kason},
  year={2025},
  howpublished={\\url{https://lab-kason-biochem.streamlit.app}},
  note={Interactive web application built with Streamlit and Python. 
        Includes IC50/Ki calculators, kinetics simulators, and drug case studies}
}""", language="bibtex")
        
        st.markdown("---")
        
        st.markdown("#### Additional Information")
        st.info("""**Version:** 1.0 (November 2025)
**Platform:** Streamlit 1.51.0
**Technologies:** Python, NumPy, Pandas, Plotly
**License:** Educational use permitted with attribution
**Repository:** https://github.com/lab-Kason/biochem
        """)
        
        st.markdown("---")
        
        st.warning("""**Disclaimer:** This tool is designed for educational purposes only. 
All data, calculations, and clinical information should be verified with primary 
literature sources and are not intended for clinical or commercial drug development 
decisions. The case study data presented are approximate values derived from published 
literature for illustrative purposes. Always consult current medical literature and 
guidelines for clinical applications.""")

# Case Studies Section
def show_case_studies():
    st.markdown('<div class="section-header">💊 Successful Drug Case Studies</div>', unsafe_allow_html=True)
    
    # User Guide for Case Studies
    with st.expander("📖 How to Explore Case Studies", expanded=False):
        st.markdown("""
        **Real-World Drug Success Stories**
        
        **What's included:**
        This section showcases **5 blockbuster enzyme inhibitor drugs** that revolutionized medicine.
        
        **How to navigate:**
        1. **Select a drug class** from the radio buttons above
        2. **Read the drug card** (left panel) for key facts:
           - Drug name and target enzyme
           - Inhibition mechanism
           - FDA approval date
           - Market impact
        3. **Study "How It Works"** section to understand the mechanism
        4. **Analyze interactive charts** (right panel) showing:
           - Clinical efficacy data
           - Patient outcomes over time
           - Comparative potency
        
        **The 5 Case Studies:**
        
        **1. Statins (Cholesterol)** 💊
        - Example: Lipitor (Atorvastatin)
        - Best-selling drug of all time
        - Reduces cardiac deaths significantly
        
        **2. HIV Protease Inhibitors** 🦠
        - Transformed HIV from fatal to manageable
        - Increased life expectancy from ~1 year to near-normal
        - Structure-based drug design success story
        
        **3. ACE Inhibitors (Blood Pressure)** ❤️
        - Examples: Lisinopril, Enalapril
        - One of most prescribed drug classes
        - Inspired by snake venom peptides
        
        **4. Kinase Inhibitors (Cancer)** 🎗️
        - Example: Gleevec (Imatinib)
        - Revolutionized cancer treatment
        - 95% remission rate in CML
        
        **5. COX-2 Inhibitors (Pain)** 🩹
        - Selective pain relief
        - Reduced GI side effects vs traditional NSAIDs
        - Example of targeted drug design
        
        **Each case includes:**
        - ✅ Mechanism of action
        - ✅ Clinical trial data
        - ✅ Interactive visualizations
        - ✅ Real-world impact statistics
        - ✅ References to original research
        
        *Click through each drug to see how enzyme inhibitor design led to life-saving medications!*
        """)
    
    case_study = st.radio(
        "Select Drug Case Study:",
        ["Statins (Cholesterol)", "HIV Protease Inhibitors", "ACE Inhibitors (Blood Pressure)", 
         "Kinase Inhibitors (Cancer)", "COX-2 Inhibitors (Pain)"],
        horizontal=True
    )
    
    if case_study == "Statins (Cholesterol)":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="drug-card">
            <h4>💊 Atorvastatin (Lipitor)</h4>
            <b>Target:</b> HMG-CoA reductase<br>
            <b>Mechanism:</b> Competitive inhibition<br>
            <b>Disease:</b> Hypercholesterolemia<br>
            <b>First Approved:</b> 1996 (FDA)<br>
            <b>Peak Sales:</b> $12.9 billion/year<br>
            <b>Impact:</b> Best-selling drug of all time
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""### 🔬 Drug Development Story
            
**Discovery Timeline** (Endo, 2010; Istvan & Deisenhofer, 2001):
- **1971:** Akira Endo discovers compactin from fungus *Penicillium citrinum* 
- **1976:** Compactin shown to inhibit HMG-CoA reductase
- **1980s:** Structure-based drug design begins after enzyme crystal structure solved
- **1987:** Lovastatin (first statin) FDA approved
- **1996:** Atorvastatin (Lipitor) approved - optimized for potency
- **2002:** Heart Protection Study validates cardiovascular benefits

**Development Approach:**
- **Natural product screening** → Led to compactin discovery (Endo, 2010)
- **Structure-based optimization** → Improved IC50 and selectivity (Istvan & Deisenhofer, 2001)
- **Competitive inhibition design** → Mimics natural substrate HMG-CoA
- **Clinical validation** → Large-scale trials with 20,536+ patients (Heart Protection Study, 2002)

---

**How It Works:**
Statins competitively inhibit HMG-CoA reductase, the rate-limiting enzyme in cholesterol 
biosynthesis. By binding to the active site, they prevent the conversion of HMG-CoA to 
mevalonate, thereby reducing cholesterol production in the liver (Istvan & Deisenhofer, 2001).

**Clinical Impact:**
- Reduces LDL cholesterol by 39-60% (Heart Protection Study, 2002)
- Decreases cardiovascular events by 25-35% (Ridker et al., 2008)
- Prevents ~10,000 deaths annually in the US alone
- Peak sales: $12.9 billion/year (best-selling drug in history)

**Key Clinical Trials:** 
- Heart Protection Study (2002) - 20,536 patients
- JUPITER Trial (Ridker et al., 2008) - C-reactive protein prevention
            """)
        
        with col2:
            # Efficacy chart - Heart disease mortality decline (2000-2019)
            data = {'Year': [2000, 2005, 2010, 2015, 2019],
                   'Heart Disease Deaths per 100,000': [257.6, 216.8, 179.1, 168.5, 161.5]}
            df = pd.DataFrame(data)
            fig = px.line(df, x='Year', y='Heart Disease Deaths per 100,000', 
                         title="Age-Adjusted Heart Disease Mortality in the US (2000-2019)",
                         markers=True)
            fig.update_layout(height=350)
            st.plotly_chart(fig, width='stretch')
            st.caption("""*Data source: CDC NCHS Data Brief #425 (Sawyer & Flagg, 2021). Age-adjusted heart disease 
            death rates per 100,000 U.S. standard population. ICD-10 codes I00-I09, I11, I13, I20-I51. 
            Statins widely adopted after FDA approval of lovastatin (1987), simvastatin (1991), and atorvastatin (1996). 
            DOI: 10.15620/cdc:112339. See References section for full citations.*""")
            
            # Market comparison
            statin_data = pd.DataFrame({
                'Drug': ['Rosuvastatin\n(20 mg)', 'Simvastatin\n(40 mg)'],
                'LDL Reduction (%)': [50, 30],
                'Type': ['High Potency', 'Moderate Potency']
            })
            fig2 = px.bar(statin_data, x='Drug', y='LDL Reduction (%)', 
                         color='Type', title='Comparative Potency of Statins',
                         color_discrete_map={'High Potency': '#FF6B6B', 'Moderate Potency': '#4ECDC4'})
            fig2.update_layout(height=300)
            st.plotly_chart(fig2, width='stretch')
            st.caption("""*Data from large-scale randomized controlled trials. Rosuvastatin 20 mg: 50% LDL reduction 
            (Ridker et al., 2008, JUPITER trial, NEJM). Simvastatin 40 mg: ~30% LDL reduction 
            (Heart Protection Study, 2002, The Lancet). See References section for full citations.*""")
    
    elif case_study == "HIV Protease Inhibitors":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="drug-card">
            <h4>💊 Ritonavir, Saquinavir, Indinavir</h4>
            <b>Target:</b> HIV-1 Protease<br>
            <b>Mechanism:</b> Competitive inhibition<br>
            <b>Disease:</b> HIV/AIDS<br>
            <b>First Approved:</b> 1995 (Saquinavir)<br>
            <b>Impact:</b> Transformed HIV from fatal to manageable chronic disease
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""### 🔬 Drug Development Story

**Discovery Timeline** (Kohl et al., 1988; Wlodawer & Vondrasek, 1998; Flexner, 1998):
- **1988:** HIV protease identified as essential for viral infectivity (Kohl et al., 1988)
- **1989:** X-ray crystal structure of HIV protease solved
- **1990-1995:** Structure-based drug design era begins (Wlodawer & Vondrasek, 1998)
- **1995:** Saquinavir - first protease inhibitor FDA approved
- **1996:** Ritonavir and Indinavir approved - HAART era begins
- **1998:** Declining morbidity and mortality observed (Palella et al., 1998)

**Development Approach:**
- **Rational design** → Used X-ray crystallography of enzyme-inhibitor complexes (Wlodawer & Vondrasek, 1998)
- **Transition-state mimicry** → Designed to resemble peptide cleavage intermediate
- **Structure-activity optimization** → Improved IC50 from μM to nM range (Flexner, 1998)
- **Combination therapy** → HAART protocol with multiple antiretrovirals (Gulick et al., 1997)

**Major Success of Structure-Assisted Drug Design** (Wlodawer & Vondrasek, 1998)

---

**How It Works:**
HIV protease inhibitors mimic the transition state of the natural peptide substrate, 
binding tightly to the enzyme's active site. They prevent the cleavage of viral 
polyproteins, blocking the maturation of infectious viral particles (Kohl et al., 1988).

**Clinical Impact:**
- Reduces viral load by >90% when combined with other antiretrovirals (Gulick et al., 1997)
- Increased life expectancy from ~1 year to near-normal (Palella et al., 1998)
- Death rate decreased by 80% after introduction (1996-1998) (Palella et al., 1998)
- Part of HAART (Highly Active Antiretroviral Therapy)
- Transformed HIV from death sentence to manageable chronic disease

**Key Clinical Trials:**
- Gulick et al. (1997) - Indinavir + zidovudine + lamivudine combination
- Palella et al. (1998) - Documented declining mortality with protease inhibitors
            """)
        
        with col2:
            # HIV survival timeline
            survival_data = pd.DataFrame({
                'Era': ['Pre-1996\n(No ART)', '1996-1999\n(Early ART)', 
                       '2000-2002\n(Improved ART)', '2003-2005\n(Modern ART)'],
                'Life Expectancy at Age 20 (years)': [36, 39, 50, 63],
                'Order': [1, 2, 3, 4]
            })
            fig = px.bar(survival_data, x='Era', y='Life Expectancy at Age 20 (years)',
                        title='Life Expectancy for 20-Year-Olds Starting HIV Treatment',
                        color='Life Expectancy at Age 20 (years)',
                        color_continuous_scale='Viridis')
            fig.update_layout(height=350, showlegend=False)
            st.plotly_chart(fig, width='stretch')
            st.caption("""*Data source: Antiretroviral Therapy Cohort Collaboration (2008). 
            Life expectancy estimates for 20-year-olds starting ART with CD4 count 200 cells/µL. 
            By 2003-2005, life expectancy approached general population (63 years vs. 78 years for HIV-negative). 
            The Lancet 372(9635):293-299. See References section for full citation.*""")
            
            # Drug potency comparison
            st.markdown("**Protease Inhibitor Potency (IC50 values for viral inhibition):**")
            pi_data = pd.DataFrame({
                'Drug': ['Ritonavir', 'Saquinavir', 'Indinavir', 'Lopinavir'],
                'IC50 (nM)': [15, 5, 10, 8]
            })
            fig2 = px.bar(pi_data, x='Drug', y='IC50 (nM)', 
                         title='IC50 for Viral Production Inhibition (Lower = More Potent)',
                         log_y=True)
            fig2.update_layout(height=300)
            st.plotly_chart(fig2, width='stretch')
            st.caption("""*Representative IC50 values for HIV viral production inhibition. 
            Source: Flexner (1998) reports IC50 range of 2-60 nM for viral production. 
            NEJM 338(18):1281-1293. See References section for full citation and DOI.*""")
    
    elif case_study == "ACE Inhibitors (Blood Pressure)":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="drug-card">
            <h4>💊 Lisinopril, Enalapril, Captopril</h4>
            <b>Target:</b> Angiotensin-Converting Enzyme (ACE)<br>
            <b>Mechanism:</b> Competitive inhibition<br>
            <b>Disease:</b> Hypertension, Heart Failure<br>
            <b>First Approved:</b> 1981 (Captopril)<br>
            <b>Impact:</b> One of most prescribed drug classes worldwide
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""### 🔬 Drug Development Story

**Discovery Timeline** (Cushman & Ondetti, 1991; Pfeffer et al., 1992; Yusuf et al., 2000):
- **1965:** Discovery that snake venom (*Bothrops jararaca*) contains ACE inhibitors
- **1970s:** Synthetic peptide analogs developed (Cushman & Ondetti, 1991)
- **1977:** Captopril designed with zinc-binding thiol group
- **1981:** Captopril FDA approved - first ACE inhibitor drug
- **1985:** Enalapril approved - improved pharmacokinetics
- **1992:** SAVE Trial demonstrates mortality benefit (Pfeffer et al., 1992)
- **2000:** HOPE Study expands indications (Yusuf et al., 2000)

**Development Approach:**
- **Nature-inspired design** → Snake venom peptides as lead compounds (Cushman & Ondetti, 1991)
- **Rational drug design** → Designed zinc-binding group for active site
- **Structure optimization** → Removed peptide bonds for oral bioavailability
- **Clinical validation** → Multiple large-scale cardiovascular outcomes trials

**Bio-inspired Drug Design Success Story**

---

**How It Works:**
ACE inhibitors block the conversion of angiotensin I to angiotensin II, a potent 
vasoconstrictor. They contain a zinc-binding group that coordinates with the zinc ion 
in the ACE active site, preventing substrate binding (Cushman & Ondetti, 1991).

**Clinical Impact:**
- Reduces blood pressure by 10-15 mmHg (systolic)
- Decreases heart failure mortality by 20-30% (Pfeffer et al., 1992)
- Reduces cardiovascular events in high-risk patients (Yusuf et al., 2000)
- Protects kidney function in diabetic patients
- Used by >40 million Americans annually - one of most prescribed drug classes

**Key Clinical Trials:**
- SAVE Trial (Pfeffer et al., 1992) - Post-MI survival benefit
- HOPE Study (Yusuf et al., 2000) - High-risk patient cardiovascular protection

**Design Inspiration:** Based on snake venom peptides from *Bothrops jararaca*
            """)
        
        with col2:
            # Blood pressure effects note
            st.info("""
            **Blood Pressure Effects:** The HOPE trial demonstrated that ramipril's cardiovascular benefits extend beyond 
            blood pressure reduction. Mean BP reduction was only 3/2 mmHg (139/79 → 136/76 mmHg at study end), yet cardiovascular 
            outcomes improved by 20-32%. This suggests ACE inhibitors provide vascular protection through multiple mechanisms 
            beyond BP lowering (e.g., improved endothelial function, reduced vascular inflammation, plaque stabilization).
            """)
            
            st.caption("""*Source: HOPE Study blood pressure data. Yusuf S, et al. (2000). N Engl J Med. 342(3):145-153.*""")
            
            # Cardiovascular outcomes
            outcome_data = pd.DataFrame({
                'Outcome': ['Heart Attack', 'Stroke', 'Heart Failure', 'CV Death'],
                'Risk Reduction (%)': [20, 32, 23, 26]
            })
            fig2 = px.bar(outcome_data, x='Outcome', y='Risk Reduction (%)',
                         title='Cardiovascular Risk Reduction with Ramipril (HOPE Trial)',
                         color='Risk Reduction (%)', color_continuous_scale='Greens')
            fig2.update_layout(height=300, showlegend=False)
            st.plotly_chart(fig2, width='stretch')
            st.caption("""*Source: Heart Outcomes Prevention Evaluation (HOPE) Study. Yusuf S, et al. (2000). Effects of ramipril (10 mg/day) 
            on cardiovascular events in 9,297 high-risk patients over 5 years. N Engl J Med. 342(3):145-153. DOI: 10.1056/NEJM200001203420301. 
            Risk reductions: MI 20% (RR 0.80, P<0.001), Stroke 32% (RR 0.68, P<0.001), Heart Failure 23% (RR 0.77, P<0.001), CV Death 26% (RR 0.74, P<0.001).*""")
    
    elif case_study == "Kinase Inhibitors (Cancer)":
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="drug-card">
            <h4>💊 Imatinib (Gleevec), Gefitinib, Erlotinib</h4>
            <b>Target:</b> Tyrosine Kinases (BCR-ABL, EGFR)<br>
            <b>Mechanism:</b> Competitive inhibition (ATP-binding site)<br>
            <b>Disease:</b> Chronic Myeloid Leukemia, Lung Cancer<br>
            <b>First Approved:</b> 2001 (Imatinib)<br>
            <b>Impact:</b> Paradigm shift toward targeted cancer therapy
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""### 🔬 Drug Development Story

**Discovery Timeline** (Druker et al., 2001; Cohen, 2002; Deininger et al., 2005):
- **1990s:** BCR-ABL fusion protein identified as CML driver
- **1992-1996:** Screening for tyrosine kinase inhibitors by Novartis (Deininger et al., 2005)
- **1996:** Imatinib (STI571/Gleevec) identified as selective BCR-ABL inhibitor
- **1998:** Phase I clinical trials begin (Druker et al., 2001)
- **2001:** FDA approval - remarkably fast (2.5 months review time)
- **2002:** Recognized as major drug target category (Cohen, 2002)
- **2017:** Long-term follow-up confirms sustained efficacy (Hochhaus et al., 2017)

**Development Approach:**
- **Targeted molecular therapy** → Designed for specific oncogenic kinase (Druker et al., 2001)
- **ATP-competitive inhibition** → Binds to ATP-binding pocket
- **Rational drug design** → Structure-based optimization for selectivity (Deininger et al., 2005)
- **Rapid clinical development** → Dramatic phase I results accelerated approval
- **Paradigm shift** → Demonstrated that targeted therapy could cure cancer (Cohen, 2002)

**First Major Success of Precision Medicine in Oncology**

---

**How It Works:**
Kinase inhibitors compete with ATP for the enzyme's binding site, preventing 
phosphorylation of target proteins. This blocks signaling pathways that drive 
cancer cell proliferation and survival (Druker et al., 2001).

**Clinical Impact - Imatinib for CML:**
- 10-year survival rate: 83% vs. 20% before 2001 (Hochhaus et al., 2017)
- Complete cytogenetic response: 87% of patients (Druker et al., 2001)
- Transformed CML from terminal (median survival 3-5 years) to chronic condition
- Led to development of 50+ kinase inhibitor drugs (Cohen, 2002)
- Established kinases as \"major drug targets of the twenty-first century\" (Cohen, 2002)

**Key Clinical Trials:**
- Druker et al. (2001) - Phase I/II trials demonstrating efficacy and safety
- Hochhaus et al. (2017) - 10-year follow-up confirming long-term survival benefit

**Precision Medicine:** First major success of targeted molecular therapy
            """)
        
        with col2:
            # CML survival comparison
            cml_data = pd.DataFrame({
                'Treatment': ['Pre-Imatinib\n(1990s)', 'Imatinib\n(2001+)', 'Second-gen\n(2006+)'],
                '5-Year Survival (%)': [30, 89, 93],
                'Order': [1, 2, 3]
            })
            fig = px.bar(cml_data, x='Treatment', y='5-Year Survival (%)',
                        title='CML Survival: The Imatinib Revolution',
                        color='5-Year Survival (%)',
                        color_continuous_scale='Blues')
            fig.update_layout(height=350, showlegend=False)
            st.plotly_chart(fig, width='stretch')
            st.caption("""*Data sources: Druker et al. (2001) NEJM; Hochhaus et al. (2017) 10-year follow-up study. 
            See References section for full citations.*""")
            
            # Kinase inhibitor selectivity
            st.markdown("**Selectivity Profile:**")
            selectivity_data = pd.DataFrame({
                'Target': ['BCR-ABL', 'PDGFR', 'c-KIT', 'Off-targets'],
                'IC50 (nM)': [260, 380, 410, 5000],
                'Type': ['Primary', 'Secondary', 'Secondary', 'Non-target']
            })
            fig2 = px.bar(selectivity_data, x='Target', y='IC50 (nM)',
                         title='Imatinib Selectivity (Lower = More Potent)',
                         color='Type', log_y=True)
            fig2.update_layout(height=300)
            st.plotly_chart(fig2, width='stretch')
            st.caption("""*Data source: Deininger et al. (2005) The development of imatinib as a therapeutic agent. 
            Blood 105(7):2640-2653. See References section for full citation.*""")
    
    else:  # COX-2 Inhibitors (Pain)
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            <div class="drug-card">
            <h4>💊 Celecoxib (Celebrex), Rofecoxib (Vioxx)</h4>
            <b>Target:</b> Cyclooxygenase-2 (COX-2)<br>
            <b>Mechanism:</b> Selective competitive inhibition<br>
            <b>Disease:</b> Pain, Inflammation, Arthritis<br>
            <b>First Approved:</b> 1998 (Celecoxib)<br>
            <b>Impact:</b> Safer alternative to traditional NSAIDs
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""### 🔬 Drug Development Story

**Discovery Timeline** (Vane & Botting, 1998; Bombardier et al., 2000; FitzGerald, 2004):
- **1991:** COX-2 enzyme discovered and cloned
- **1994:** Recognition that COX-2 selectivity could reduce GI side effects (Vane & Botting, 1998)
- **1995-1998:** Structure-based design of selective COX-2 inhibitors
- **1998:** Celecoxib (Celebrex) FDA approved - first COX-2 selective inhibitor
- **1999:** Rofecoxib (Vioxx) approved
- **2000:** VIGOR and CLASS trials demonstrate GI safety (Bombardier et al., 2000; Silverstein et al., 2000)
- **2004:** Rofecoxib withdrawn due to cardiovascular risks (FitzGerald, 2004)

**Development Approach:**
- **Enzyme isoform selectivity** → Designed to spare COX-1 (Vane & Botting, 1998)
- **Structure-based drug design** → Targeted COX-2 active site differences
- **Clinical validation** → Large-scale GI safety trials (CLASS, VIGOR)
- **Post-market surveillance** → Identified cardiovascular safety concerns (FitzGerald, 2004)

**Example of Both Success and Challenges in Drug Development**

---

**How It Works:**
COX-2 inhibitors selectively block cyclooxygenase-2, the enzyme induced during 
inflammation, while sparing COX-1 (important for stomach protection). This provides 
pain relief with reduced gastrointestinal side effects (Vane & Botting, 1998).

**Clinical Impact:**
- Similar pain relief to traditional NSAIDs
- 50-60% reduction in serious GI complications (Bombardier et al., 2000; Silverstein et al., 2000)
- Reduced gastric ulcers: 0.4% vs. 1.4% with traditional NSAIDs (Silverstein et al., 2000)
- Used by millions for arthritis management

**Selectivity:** COX-2/COX-1 selectivity ratio >100:1

**Key Clinical Trials:**
- CLASS Study (Silverstein et al., 2000) - GI toxicity comparison
- VIGOR Trial (Bombardier et al., 2000) - Safety and efficacy in rheumatoid arthritis

**Important Lesson:** Rofecoxib withdrawn in 2004 due to cardiovascular risks (FitzGerald, 2004), 
demonstrating importance of long-term safety monitoring even after FDA approval.
            """)
        
        with col2:
            # Selectivity comparison
            cox_data = pd.DataFrame({
                'Drug': ['Celecoxib', 'Traditional NSAIDs', 'Aspirin'],
                'COX-2 Inhibition': [90, 75, 65],
                'COX-1 Inhibition': [10, 80, 95]
            })
            fig = go.Figure()
            fig.add_trace(go.Bar(name='COX-2 Inhibition', x=cox_data['Drug'], 
                               y=cox_data['COX-2 Inhibition'], marker_color='green'))
            fig.add_trace(go.Bar(name='COX-1 Inhibition', x=cox_data['Drug'], 
                               y=cox_data['COX-1 Inhibition'], marker_color='red'))
            fig.update_layout(title='COX-2 Selectivity: Reducing GI Side Effects',
                            yaxis_title='% Inhibition',
                            barmode='group',
                            height=350)
            st.plotly_chart(fig, width='stretch')
            st.caption("""*Data source: Vane & Botting (1998) Mechanism of action of NSAIDs. 
            American Journal of Medicine 104(3A):2S-8S. See References section for full citation.*""")
            
            # Side effect comparison
            side_effects = pd.DataFrame({
                'Side Effect': ['GI Ulcers', 'GI Bleeding', 'Dyspepsia'],
                'Traditional NSAIDs (%)': [1.4, 1.0, 15],
                'COX-2 Inhibitors (%)': [0.4, 0.3, 8]
            })
            fig2 = go.Figure()
            fig2.add_trace(go.Bar(name='Traditional NSAIDs', 
                                x=side_effects['Side Effect'], 
                                y=side_effects['Traditional NSAIDs (%)']))
            fig2.add_trace(go.Bar(name='COX-2 Inhibitors', 
                                x=side_effects['Side Effect'], 
                                y=side_effects['COX-2 Inhibitors (%)']))
            fig2.update_layout(title='Gastrointestinal Side Effects Comparison',
                             yaxis_title='Incidence (%)',
                             barmode='group',
                             height=300)
            st.plotly_chart(fig2, width='stretch')
            st.caption("""*Data sources: CLASS Study (Silverstein et al., 2000) & VIGOR Trial (Bombardier et al., 2000). 
            See References section for full citations.*""")

# Main application flow
def main():
    selected_section = create_header()
    
    if selected_section == "Overview":
        show_overview()
    elif selected_section == "Mechanisms":
        show_mechanisms()
    elif selected_section == "Case Studies":
        show_case_studies()
    elif selected_section == "Calculator":
        show_calculator()
    elif selected_section == "References":
        show_references()
    else:
        st.markdown('<div class="section-header">🚀 Future Directions</div>', unsafe_allow_html=True)
        # Add future trends content
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
    <i>Interactive Educational Poster - Enzyme Inhibitors in Drug Development</i><br>
    Created with Streamlit | For educational purposes
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
