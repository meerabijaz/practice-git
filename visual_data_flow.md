# Data Flow Diagram: Real-time Presentation Confidence Scoring System

## System Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    PRESENTATION CONFIDENCE SCORING SYSTEM                                      │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Layer Architecture

```
INPUT LAYER    →    PROCESSING LAYER    →    ANALYSIS LAYER    →    SCORING LAYER    →    OUTPUT LAYER
    ┌─────┐              ┌─────┐               ┌─────┐              ┌─────┐             ┌─────┐
    │  🎥 │              │ 🔧  │               │ 🧠  │              │ ⚡  │             │ 📊  │
    │📱🎤 │              │     │               │     │              │     │             │     │
    └─────┘              └─────┘               └─────┘              └─────┘             └─────┘
```

## Detailed Data Flow

### 1. Input Capture Layer
```
┌──────────────┐                    ┌──────────────┐
│   WEBCAM     │ ──── Video ────→   │ Video Buffer │
│  📹 Camera   │     Stream         │   (Queue)    │
│  1080p@30fps │                    │              │
└──────────────┘                    └──────────────┘
                                           │
                                           ▼
┌──────────────┐                    ┌──────────────┐
│ MICROPHONE   │ ──── Audio ────→   │ Audio Buffer │
│  🎤 Audio    │     Stream         │   (Queue)    │
│  44.1kHz     │                    │              │
└──────────────┘                    └──────────────┘
```

### 2. Processing Layer
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Video Buffer │────→│    OpenCV    │────→│ Processed    │
│              │     │ Frame Capture│     │ Video Frames │
└──────────────┘     │ Preprocessing│     │              │
                     └──────────────┘     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │ - Resize     │
                     │ - Denoise    │
                     │ - Color Conv │
                     └──────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Audio Buffer │────→│   Librosa    │────→│ Audio        │
│              │     │ Audio Proc.  │     │ Segments     │
└──────────────┘     │ Windowing    │     │              │
                     └──────────────┘     └──────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │ - FFT        │
                     │ - Windowing  │
                     │ - Filtering  │
                     └──────────────┘
```

### 3. Analysis Layer
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Processed    │────→│  MediaPipe   │────→│ Body Posture │
│ Video Frames │     │ Pose Tracking│     │ Keypoints    │
└──────────────┘     └──────────────┘     └──────────────┘
                            │                     │
                            ▼                     ▼
                     ┌──────────────┐     ┌──────────────┐
                     │ 33 Landmarks │     │ Movement     │
                     │ 3D Coords    │     │ Analysis     │
                     │ Per Frame    │     │              │
                     └──────────────┘     └──────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Audio        │────→│ Feature      │────→│ Vocal        │
│ Segments     │     │ Extraction   │     │ Features     │
└──────────────┘     └──────────────┘     └──────────────┘
                            │                     │
                            ▼                     ▼
                     ┌──────────────┐     ┌──────────────┐
                     │ - Pitch F0   │     │ - Stability  │
                     │ - Loudness   │     │ - Variance   │
                     │ - Jitter     │     │ - Consistency│
                     └──────────────┘     └──────────────┘
```

### 4. Confidence Scoring Engine
```
┌──────────────┐     ┌──────────────────────────────┐     ┌──────────────┐
│ Movement     │────→│                              │     │              │
│ Analysis     │     │     CONFIDENCE SCORING       │     │              │
└──────────────┘     │         ENGINE               │     │              │
                     │                              │     │              │
┌──────────────┐     │  ┌─────────────────────────┐ │     │              │
│ Vocal        │────→│  │ Physical Confidence     │ │────→│ Final Score  │
│ Features     │     │  │ • Movement variance     │ │     │ (0-100)      │
└──────────────┘     │  │ • Posture stability     │ │     │              │
                     │  │ • Hand steadiness       │ │     │              │
                     │  └─────────────────────────┘ │     │              │
                     │                              │     │              │
                     │  ┌─────────────────────────┐ │     │              │
                     │  │ Vocal Confidence        │ │     │              │
                     │  │ • Pitch stability       │ │     │              │
                     │  │ • Volume consistency    │ │     │              │
                     │  │ • Speech smoothness     │ │     │              │
                     │  └─────────────────────────┘ │     │              │
                     │                              │     │              │
                     │  Algorithm:                  │     │              │
                     │  Score = 0.4×Physical +      │     │              │
                     │          0.6×Vocal           │     │              │
                     └──────────────────────────────┘     └──────────────┘
```

### 5. Output Layer
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Final Score  │────→│   Tkinter    │────→│ Real-time    │
│ (0-100)      │     │ GUI Display  │     │ Feedback     │
└──────────────┘     │              │     │              │
                     │ OR           │     │ • Score      │
                     │              │     │ • Trend      │
                     │ Console      │     │ • Colors     │
                     │ Output       │     │ • History    │
                     └──────────────┘     └──────────────┘
```

## Tech Stack Data Flow Summary

| Component | Input | Processing | Output | Update Rate |
|-----------|-------|------------|--------|-------------|
| **Webcam** | Hardware capture | Frame acquisition | Raw video stream | 30 FPS |
| **Microphone** | Hardware capture | Audio sampling | Raw audio stream | 44.1 kHz |
| **OpenCV** | Video stream | Frame processing, preprocessing | Processed frames | 30 FPS |
| **Librosa** | Audio stream | Audio analysis, windowing | Audio features | 21.5 Hz |
| **MediaPipe** | Processed frames | Pose estimation | Body landmarks | 30 FPS |
| **Feature Extraction** | Audio features | Mathematical analysis | Confidence metrics | 30 Hz |
| **Scoring Engine** | All metrics | Weighted combination | Final score | 1 Hz |
| **Tkinter/Console** | Final score | Display rendering | User feedback | 1 Hz |

## Data Transformation Pipeline

```
Raw Streams → Processing → Feature Extraction → Analysis → Scoring → Display
     ↓             ↓              ↓              ↓         ↓         ↓
 Binary Data → Numpy Arrays → Vector Data → Metrics → Score → Visual
   (MB/s)       (KB/frame)    (Bytes)      (Float)   (Int)   (GUI)
```

## Performance Characteristics

- **Total Latency**: < 100ms
- **Memory Usage**: < 200MB
- **CPU Usage**: Single-core optimized
- **Storage**: Minimal (temp buffers only)
- **Network**: None (local processing)

## Error Handling Flow

```
Input Failure → Fallback Mode → Degraded Operation → User Notification
     ↓               ↓                ↓                    ↓
Camera Lost → Audio Only → Lower Accuracy → Warning Message
Audio Lost → Video Only → Partial Score → Status Update
Both Lost → Error State → System Halt → Restart Required
```

This data flow diagram shows how your real-time presentation confidence scoring system processes data through each layer of the tech stack, from raw sensor input to final user feedback.