def generate_report(prediction):

    report = f"""
X-RAY ANALYSIS REPORT

Finding:
{prediction['finding']}

Confidence:
{prediction['confidence']}
"""

    return report
