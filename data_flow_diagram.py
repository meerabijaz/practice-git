import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Color scheme
colors = {
    'input': '#E3F2FD',      # Light blue
    'processing': '#FFF3E0',  # Light orange
    'analysis': '#E8F5E8',    # Light green
    'scoring': '#F3E5F5',     # Light purple
    'output': '#FFEBEE'       # Light red
}

# Define components with positions and sizes
components = {
    # Input Layer
    'webcam': {'pos': (1, 10), 'size': (2, 1), 'label': 'Webcam\n(Video Input)', 'color': colors['input']},
    'microphone': {'pos': (1, 8), 'size': (2, 1), 'label': 'Microphone\n(Audio Input)', 'color': colors['input']},
    
    # Processing Layer
    'opencv': {'pos': (5, 10), 'size': (2.5, 1), 'label': 'OpenCV\n(Video Processing)', 'color': colors['processing']},
    'librosa': {'pos': (5, 8), 'size': (2.5, 1), 'label': 'Librosa\n(Audio Processing)', 'color': colors['processing']},
    
    # Analysis Layer
    'mediapipe': {'pos': (9, 10), 'size': (2.5, 1), 'label': 'MediaPipe\n(Body Posture\nTracking)', 'color': colors['analysis']},
    'audio_features': {'pos': (9, 8), 'size': (2.5, 1), 'label': 'Audio Feature\nExtraction\n(Pitch, Loudness)', 'color': colors['analysis']},
    
    # Scoring Engine
    'confidence_engine': {'pos': (13, 9), 'size': (2.5, 2), 'label': 'Confidence\nScoring Engine\n(AI Algorithms)', 'color': colors['scoring']},
    
    # Output Layer
    'display': {'pos': (7, 5), 'size': (3, 1.5), 'label': 'Real-time Display\n(Tkinter/Console)\nConfidence Score', 'color': colors['output']},
    
    # Data stores
    'video_data': {'pos': (5, 6), 'size': (1.5, 0.8), 'label': 'Video\nFrames', 'color': '#F5F5F5'},
    'audio_data': {'pos': (5, 4.5), 'size': (1.5, 0.8), 'label': 'Audio\nSamples', 'color': '#F5F5F5'},
    'posture_data': {'pos': (9, 6), 'size': (1.5, 0.8), 'label': 'Posture\nKeypoints', 'color': '#F5F5F5'},
    'vocal_data': {'pos': (9, 4.5), 'size': (1.5, 0.8), 'label': 'Vocal\nFeatures', 'color': '#F5F5F5'}
}

# Draw components
for comp_name, comp_data in components.items():
    x, y = comp_data['pos']
    w, h = comp_data['size']
    
    # Create rounded rectangle
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.1",
        facecolor=comp_data['color'],
        edgecolor='black',
        linewidth=1.5
    )
    ax.add_patch(box)
    
    # Add text
    ax.text(x + w/2, y + h/2, comp_data['label'], 
            ha='center', va='center', fontsize=9, fontweight='bold')

# Define data flows with labels
flows = [
    # Input to Processing
    {'from': (3, 10.5), 'to': (5, 10.5), 'label': 'Live Video\nStream', 'color': 'blue'},
    {'from': (3, 8.5), 'to': (5, 8.5), 'label': 'Live Audio\nStream', 'color': 'green'},
    
    # Processing to intermediate data
    {'from': (6.25, 10), 'to': (5.75, 6.8), 'label': 'Processed\nFrames', 'color': 'blue'},
    {'from': (6.25, 8), 'to': (5.75, 5.3), 'label': 'Audio\nSegments', 'color': 'green'},
    
    # Processing to Analysis
    {'from': (7.5, 10.5), 'to': (9, 10.5), 'label': 'Video Data', 'color': 'blue'},
    {'from': (7.5, 8.5), 'to': (9, 8.5), 'label': 'Audio Data', 'color': 'green'},
    
    # Analysis to feature data
    {'from': (10.25, 10), 'to': (9.75, 6.8), 'label': 'Body\nMovements', 'color': 'purple'},
    {'from': (10.25, 8), 'to': (9.75, 5.3), 'label': 'Pitch &\nLoudness', 'color': 'orange'},
    
    # Feature data to Confidence Engine
    {'from': (10.5, 6.4), 'to': (13, 9.5), 'label': 'Physical\nConfidence\nMetrics', 'color': 'purple'},
    {'from': (10.5, 4.9), 'to': (13, 9), 'label': 'Vocal\nConfidence\nMetrics', 'color': 'orange'},
    
    # Confidence Engine to Display
    {'from': (13.5, 9), 'to': (8.5, 6.5), 'label': 'Real-time\nConfidence\nScore', 'color': 'red'}
]

# Draw arrows and labels
for flow in flows:
    from_pos = flow['from']
    to_pos = flow['to']
    
    # Calculate arrow properties
    dx = to_pos[0] - from_pos[0]
    dy = to_pos[1] - from_pos[1]
    
    # Draw arrow
    arrow = patches.FancyArrowPatch(
        from_pos, to_pos,
        arrowstyle='->', 
        mutation_scale=15,
        color=flow['color'],
        linewidth=2
    )
    ax.add_patch(arrow)
    
    # Add label at midpoint
    mid_x = (from_pos[0] + to_pos[0]) / 2
    mid_y = (from_pos[1] + to_pos[1]) / 2 + 0.2
    
    ax.text(mid_x, mid_y, flow['label'], 
            ha='center', va='center', fontsize=7, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

# Add title
ax.text(8, 11.5, 'Data Flow Diagram: Real-time Presentation Confidence Scoring System', 
        ha='center', va='center', fontsize=16, fontweight='bold')

# Add layer labels
ax.text(0.5, 9, 'INPUT\nLAYER', ha='center', va='center', fontsize=10, fontweight='bold', rotation=90)
ax.text(4, 9, 'PROCESSING\nLAYER', ha='center', va='center', fontsize=10, fontweight='bold', rotation=90)
ax.text(8, 9, 'ANALYSIS\nLAYER', ha='center', va='center', fontsize=10, fontweight='bold', rotation=90)
ax.text(12, 9, 'SCORING\nLAYER', ha='center', va='center', fontsize=10, fontweight='bold', rotation=90)
ax.text(15.5, 5.75, 'OUTPUT\nLAYER', ha='center', va='center', fontsize=10, fontweight='bold', rotation=90)

# Add legend
legend_elements = [
    plt.Rectangle((0, 0), 1, 1, facecolor='blue', alpha=0.7, label='Video Data Flow'),
    plt.Rectangle((0, 0), 1, 1, facecolor='green', alpha=0.7, label='Audio Data Flow'),
    plt.Rectangle((0, 0), 1, 1, facecolor='purple', alpha=0.7, label='Physical Analysis'),
    plt.Rectangle((0, 0), 1, 1, facecolor='orange', alpha=0.7, label='Vocal Analysis'),
    plt.Rectangle((0, 0), 1, 1, facecolor='red', alpha=0.7, label='Confidence Score')
]

ax.legend(handles=legend_elements, loc='lower left', bbox_to_anchor=(0, 0))

# Add technical details box
tech_details = """
TECHNICAL SPECIFICATIONS:
• Video: 30 FPS capture via OpenCV
• Audio: 44.1 kHz sampling rate
• Processing: Real-time analysis (<100ms latency)
• Features: Pitch stability, loudness, body movement
• Output: Confidence score (0-100) updated every second
"""

ax.text(1, 2.5, tech_details, fontsize=8, 
        bbox=dict(boxstyle="round,pad=0.5", facecolor='#F0F0F0', alpha=0.9),
        verticalalignment='top')

plt.tight_layout()
plt.savefig('/workspace/confidence_scoring_data_flow.png', dpi=300, bbox_inches='tight')
plt.show()

print("Data Flow Diagram created successfully!")
print("File saved as: confidence_scoring_data_flow.png")