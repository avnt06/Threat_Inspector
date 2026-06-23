from utils import get_attack_severity, get_attack_vector, get_cvss_score, get_exploitablity_score, get_impact_score
import textwrap


def display_cve(cve):
    print("="*50)
    print(f"CVE ID                  : {cve['id']}")
    print(f"CVSS Score              : {get_cvss_score(cve)}")
    print(f"Attack Vector           : {get_attack_vector(cve)}")
    print(f"Severity                : {get_attack_severity(cve)}")
    print(f"Exploitability score    : {get_exploitablity_score(cve)}")
    print(f"Impact Score            : {get_impact_score(cve)}")
    print(f"Published               : {cve['published']}")
    print(f"Last Modified           : {cve['lastModified']}")
    print(f"Status                  : {cve['vulnStatus']}")
    print(f"Source                  : {cve['sourceIdentifier']}")
    print(F"\nDescription: \n {textwrap.fill(cve.get("descriptions")[0]['value'], width=80)}")
    print(f"\nReference: ")
    for ref in cve["references"][:3]:
        print(f"- {ref["url"]}")
    print("="*50)