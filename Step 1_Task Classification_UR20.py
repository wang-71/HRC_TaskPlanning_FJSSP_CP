import csv
from datetime import datetime

scores_table_section1 = {
    'Weight': {
        '> 87.5% Payload': 0,
        '70-87.5% Payload': 0.25,
        '50-70% Payload': 0.5,
        '25-50% Payload': 0.75,
        '<25% Payload': 1
    },

    'Shape': {
        'Hand-like': 0,
        '3-Finger': 0.5,
        '2-Finger or Vacuum': 1
    },

    'Stability': {
        'Shapeless': 0,
        'Deformation at Low Force': 0.25,
        'Deformation at High Force': 0.75,
        'Stable': 1
    },
    'Fragility': {
        'Sensitive': 0,
        'Damage at Low Force': 0.25,
        'Damage at High Force': 0.75,
        'Robust': 1
    }
}

scores_table_section2 = {

    'Connection Method': {
        'Welding & Gluing': 0.25,
        'Screwing & Nailing': 0.75,
        'Non-Connectable/No Connection': 1
    }
}

scores_table_section3 = {
    'Storage Arrangement': {
        'Autonomous detection Required': 0,
        'Fiducial Markers Attached': 0.5,
        'Known Identity, Position, and Orientation of Components': 1
    }
}

scores_table_section4 = {
    'Chance of Workspace Conflict': {
        'Potential Conflict': 0.25,
        'No Potential Conflict': 1
    }
}

def calculate_total_score(features, scores_table):
    total_score = 0
    for category, feature in features.items():
        total_score += scores_table[category][feature]
    return total_score

def match_weight_score(payload, weight):
    ratio = weight / payload
    if ratio > 0.875:
        return '> 87.5% Payload'
    elif 0.7 < ratio <= 0.875:
        return '70-87.5% Payload'
    elif 0.5 < ratio <= 0.7:
        return '50-70% Payload'
    elif 0.25 < ratio <= 0.5:
        return '25-50% Payload'
    else:
        return '<25% Payload'

components = [
    {
        'name': 'Joist 1', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 2', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 3', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 4', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 5', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 6', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 7', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 8', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 9', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 10', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 11', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 12', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 13', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 14', 'robot_distance': 1.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Joist 15', 'robot_distance': 1.5, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },

    {
        'name': 'Joist 16', 'robot_distance': 0.9, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components', 'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },

    {
        'name': 'Joist 17', 'robot_distance': 0.8, 'robot_reach': 1.75, 'payload': 20, 'weight': 13.28,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 18', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 19', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 20', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 21', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 22', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 23', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 24', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Joist 25', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 10.92,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Blocking 26', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 27', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 28', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 29', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 30', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 31', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 32', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 33', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 34', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 35', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 36', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 37', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 38', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 39', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 40', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 41', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 42', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 43', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 44', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 45', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 46', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 47', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 48', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 49', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 50', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 51', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 52', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 53', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 54', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 55', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 56', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Blocking 57', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.72,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Deformation at High Force', 'Fragility': 'Damage at High Force',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Non-Connectable/No Connection',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 58', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components', 'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Conn 59', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Conn 60', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Conn 61', 'robot_distance': 1.3, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 62', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Conn 63', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Conn 64', 'robot_distance': 0.7, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'No Potential Conflict'
    },
    {
        'name': 'Conn 65', 'robot_distance': 1.3, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 66', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 67', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 68', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 69', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 70', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
    {
        'name': 'Conn 71', 'robot_distance': 1.2, 'robot_reach': 1.75, 'payload': 20, 'weight': 3.3,
        'Shape': '2-Finger or Vacuum', 'Stability': 'Stable', 'Fragility': 'Robust',
        'Storage Arrangement': 'Known Identity, Position, and Orientation of Components',
        'Connection Method': 'Screwing & Nailing',
        'Chance of Workspace Conflict': 'Potential Conflict'
    },
]
results = []

for component in components:
    total_score_1 = total_score_2 = total_score_3 = total_score_4 = 0
    reason = [] 

    # Weight and Arm Reach
    if component['weight'] > component['payload']:
        reason.append('weight > payload')
    if component['robot_distance'] > component['robot_reach']:
        reason.append('robot_distance > robot_reach')

    if reason:
        task_type = 'Human Only'
        average_score = 0  
        reason = ' and '.join(reason)  
    else:
 
        weight_category = match_weight_score(component['payload'], component['weight'])

        # Section 1
        features_1 = {
            'Weight': weight_category,
            'Shape': component['Shape'],
            'Stability': component['Stability'],
            'Fragility': component['Fragility']
        }
        total_score_1 = calculate_total_score(features_1, scores_table_section1)

        # Section 2
        features_2 = {
            'Connection Method': component['Connection Method']
        }
        total_score_2 = calculate_total_score(features_2, scores_table_section2)

        # Section 3
        features_3 = {
            'Storage Arrangement': component['Storage Arrangement']
        }
        total_score_3 = calculate_total_score(features_3, scores_table_section3)

        # Section 4
        features_4 = {
            'Chance of Workspace Conflict': component['Chance of Workspace Conflict']
        }
        total_score_4 = calculate_total_score(features_4, scores_table_section4)

        average_score = (total_score_1 / 4 + total_score_2 + total_score_3 + total_score_4) / 4

        # Classify as "Human or Robot" and "Human Only"
        task_type = 'Human or Robot' if average_score >= 0.7 else 'Human Only'
        reason = 'N/A'  

    # Results
    results.append({
        'Component Name': component['name'],
        'Component': total_score_1 / 4,
        'Connection': total_score_2,
        'Storage': total_score_3,
        'Workspace': total_score_4,
        'Average Score': average_score,
        'Task Type': task_type,
        'Reason': reason  
    })

# Get current time
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f'components_scores_{current_time}.csv'

# Save as csv file
with open(filename, 'w', newline='') as csvfile:
    fieldnames = ['Component Name', 'Component', 'Connection', 'Storage', 'Workspace',
                  'Average Score', 'Task Type', 'Reason'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)

print(f"Results saved to {filename}")
