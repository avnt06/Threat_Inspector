
def get_attack_vector(cve):
    if "cvssMetricV31" in cve["metrics"]:
        attvec = cve["metrics"]["cvssMetricV31"][0]["cvssData"]["accessVector"]

    elif "cvssMetricV30" in cve["metrics"]:
        attvec = cve["metrics"]["cvssMetricV30"][0]["cvssData"]["accessVector"]

    elif "cvssMetricV2" in cve["metrics"]:
        attvec = cve["metrics"]["cvssMetricV2"][0]["cvssData"]["accessVector"]

    else:
        attvec = "N/A"

    return attvec


def get_attack_severity(cve):
    if "cvssMetricV31" in cve["metrics"]:
        svrty = cve["metrics"]["cvssMetricV31"][0]["baseSeverity"]

    elif "cvssMetricV30" in cve["metrics"]:
        svrty = cve["metrics"]["cvssMetricV30"][0]["baseSeverity"]

    elif "cvssMetricV2" in cve["metrics"]:
        svrty = cve["metrics"]["cvssMetricV2"][0]["baseSeverity"]

    else:
        svrty = "N/A"

    return svrty



def get_exploitablity_score(cve):
    if "cvssMetricV31" in cve["metrics"]:
        explscore = cve["metrics"]["cvssMetricV31"][0]["exploitabilityScore"]

    elif "cvssMetricV30" in cve["metrics"]:
        explscore = cve["metrics"]["cvssMetricV30"][0]["exploitabilityScore"]

    elif "cvssMetricV2" in cve["metrics"]:
        explscore = cve["metrics"]["cvssMetricV2"][0]["exploitabilityScore"]

    else:
        explscore = "N/A"

    return explscore

    
def get_impact_score(cve):
    if "cvssMetricV31" in cve["metrics"]:
        impactscore = cve["metrics"]["cvssMetricV31"][0]["impactScore"]

    elif "cvssMetricV30" in cve["metrics"]:
        impactscore = cve["metrics"]["cvssMetricV30"][0]["impactScore"]

    elif "cvssMetricV2" in cve["metrics"]:
        impactscore = cve["metrics"]["cvssMetricV2"][0]["impactScore"]

    else:
        impactscore = "N/A"

    return impactscore

def get_cvss_score(cve):
    if "cvssMetricV31" in cve["metrics"]:
        score = cve["metrics"]["cvssMetricV31"][0]["cvssData"]["baseScore"]

    elif "cvssMetricV30" in cve["metrics"]:
        score = cve["metrics"]["cvssMetricV30"][0]["cvssData"]["baseScore"]

    elif "cvssMetricV2" in cve["metrics"]:
        score = cve["metrics"]["cvssMetricV2"][0]["cvssData"]["baseScore"]

    else:
        score = "N/A"

    return score