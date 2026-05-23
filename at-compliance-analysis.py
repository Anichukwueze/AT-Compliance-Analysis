import datetime
from typing import Dict, List, Optional, Tuple, Union
import uuid
import random
import statistics
import json
from dataclasses import dataclass

@dataclass
class Campaign:
    """Class to represent a multi-channel marketing campaign."""
    name: str
    channels: List[str]  # e.g., ["Email", "Social Media", "SMS"]
    markets: List[str]   # e.g., ["US", "EU", "APAC"]
    status: str         # e.g., "Draft", "Under Review", "Approved", "Rejected"
    start_date: str
    end_date: str

@dataclass
class Risk:
    """Class to represent a detected risk with severity and mitigation."""
    description: str
    category: str       # e.g., "Regulatory", "Reputational", "Data Privacy"
    severity: str       # e.g., "Low", "Medium", "High", "Critical"
    likelihood: int     # 1-5 scale
    impact: int         # 1-5 scale
    mitigation: Optional[str] = None

@dataclass
class Policy:
    """Class to represent a compliance policy."""
    title: str
    category: str       # e.g., "Digital Marketing", "Data Use", "Vendor Oversight"
    requirements: List[str]
    enforcement_date: str
    status: str         # e.g., "Draft", "Active", "Retired"

@dataclass
class Dashboard:
    """Class to represent an automated compliance dashboard."""
    name: str
    metrics: List[str]  # e.g., ["Risk Count", "Campaign Approval Rate"]
    data_sources: List[str]
    update_frequency: str

class ATTComplianceAnalyst:
    def __init__(self):
        # Campaigns: {campaign_id: Campaign}
        self.campaigns: Dict[str, Campaign] = {}

        # Risks: {risk_id: Risk}
        self.risks: Dict[str, Risk] = {}

        # Statistical Models: {model_id: {"name": str, "type": str, "parameters": Dict, "accuracy": float}}
        self.statistical_models: Dict[str, Dict] = {}

        # Predictive Analytics: {analysis_id: {"name": str, "model_id": str, "results": Dict, "date": str}}
        self.predictive_analytics: Dict[str, Dict] = {}

        # Dashboards: {dashboard_id: Dashboard}
        self.dashboards: Dict[str, Dashboard] = {}

        # International Laws: {law_id: {"name": str, "region": str, "category": str, "impact": str, "compliance_status": str}}
        self.international_laws: Dict[str, Dict] = {}

        # Policies: {policy_id: Policy}
        self.policies: Dict[str, Policy] = {}

        # Vendors: {vendor_id: {"name": str, "category": str, "compliance_status": str, "risk_level": str}}
        self.vendors: Dict[str, Dict] = {}

        # Data Flows: {flow_id: {"source": str, "destination": str, "data_type": str, "compliance_status": str}}
        self.data_flows: Dict[str, Dict] = {}

        # Audit Logs: List[Dict]
        self.audit_logs: List[Dict] = {}

        # Next IDs
        self.next_campaign_id = 1
        self.next_risk_id = 1
        self.next_model_id = 1
        self.next_analysis_id = 1
        self.next_dashboard_id = 1
        self.next_law_id = 1
        self.next_policy_id = 1
        self.next_vendor_id = 1
        self.next_flow_id = 1

    # --- Campaign Management ---
    def create_campaign(self, name: str, channels: List[str], markets: List[str], start_date: str, end_date: str) -> str:
        """Create a new multi-channel marketing campaign."""
        campaign_id = f"CAMP{self.next_campaign_id}"
        self.next_campaign_id += 1
        self.campaigns[campaign_id] = Campaign(
            name=name,
            channels=channels,
            markets=markets,
            status="Draft",
            start_date=start_date,
            end_date=end_date
        )
        self._log_activity("campaign_created", {
            "campaign_id": campaign_id,
            "name": name,
            "channels": channels,
            "markets": markets
        })
        return f"Campaign '{name}' created with ID: {campaign_id}"

    def submit_campaign_for_review(self, campaign_id: str) -> str:
        """Submit a campaign for regulatory and reputational risk review."""
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id].status = "Under Review"
            self._log_activity("campaign_submitted", {"campaign_id": campaign_id})
            return f"Campaign {campaign_id} submitted for review."
        return f"Campaign ID {campaign_id} not found."

    def approve_campaign(self, campaign_id: str, approver: str) -> str:
        """Approve a campaign after risk review."""
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id].status = "Approved"
            self._log_activity("campaign_approved", {
                "campaign_id": campaign_id,
                "approver": approver
            })
            return f"Campaign {campaign_id} approved by {approver}."
        return f"Campaign ID {campaign_id} not found."

    def reject_campaign(self, campaign_id: str, reason: str) -> str:
        """Reject a campaign due to risks."""
        if campaign_id in self.campaigns:
            self.campaigns[campaign_id].status = "Rejected"
            self._log_activity("campaign_rejected", {
                "campaign_id": campaign_id,
                "reason": reason
            })
            return f"Campaign {campaign_id} rejected. Reason: {reason}"
        return f"Campaign ID {campaign_id} not found."

    # --- Risk Detection ---
    def detect_risk(self, description: str, category: str, severity: str, likelihood: int, impact: int, campaign_id: Optional[str] = None) -> str:
        """Detect and log a new risk."""
        if likelihood < 1 or likelihood > 5 or impact < 1 or impact > 5:
            return "Likelihood and impact must be between 1 and 5."

        risk_id = f"RISK{self.next_risk_id}"
        self.next_risk_id += 1
        self.risks[risk_id] = Risk(
            description=description,
            category=category,
            severity=severity,
            likelihood=likelihood,
            impact=impact
        )
        self._log_activity("risk_detected", {
            "risk_id": risk_id,
            "description": description,
            "category": category,
            "severity": severity,
            "campaign_id": campaign_id
        })
        if campaign_id:
            self._link_risk_to_campaign(risk_id, campaign_id)
        return f"Risk '{description}' detected with ID: {risk_id}. Severity: {severity}, Score: {likelihood * impact}"

    def _link_risk_to_campaign(self, risk_id: str, campaign_id: str) -> None:
        """Link a risk to a campaign."""
        if campaign_id in self.campaigns and risk_id in self.risks:
            if "risks" not in self.campaigns[campaign_id].__dict__:
                self.campaigns[campaign_id].__dict__["risks"] = []
            self.campaigns[campaign_id].__dict__["risks"].append(risk_id)

    def add_mitigation(self, risk_id: str, mitigation: str) -> str:
        """Add a mitigation strategy to a risk."""
        if risk_id in self.risks:
            self.risks[risk_id].mitigation = mitigation
            self._log_activity("mitigation_added", {
                "risk_id": risk_id,
                "mitigation": mitigation
            })
            return f"Mitigation added to Risk {risk_id}: {mitigation}"
        return f"Risk ID {risk_id} not found."

    # --- Statistical Modeling ---
    def build_statistical_model(self, name: str, model_type: str, parameters: Dict) -> str:
        """Build a statistical model for risk detection."""
        model_id = f"MODEL{self.next_model_id}"
        self.next_model_id += 1
        self.statistical_models[model_id] = {
            "name": name,
            "type": model_type,
            "parameters": parameters,
            "accuracy": 0.0,
            "last_trained": None
        }
        self._log_activity("model_built", {
            "model_id": model_id,
            "name": name,
            "type": model_type
        })
        return f"Statistical Model '{name}' built with ID: {model_id}"

    def train_model(self, model_id: str, accuracy: float) -> str:
        """Train a statistical model and update its accuracy."""
        if model_id in self.statistical_models:
            self.statistical_models[model_id]["accuracy"] = accuracy
            self.statistical_models[model_id]["last_trained"] = datetime.datetime.now().strftime("%Y-%m-%d")
            self._log_activity("model_trained", {
                "model_id": model_id,
                "accuracy": accuracy
            })
            return f"Model {model_id} trained with accuracy: {accuracy}%"
        return f"Model ID {model_id} not found."

    # --- Predictive Analytics ---
    def run_predictive_analysis(self, name: str, model_id: str, results: Dict) -> str:
        """Run a predictive analytics analysis using a statistical model."""
        if model_id in self.statistical_models:
            analysis_id = f"ANALYSIS{self.next_analysis_id}"
            self.next_analysis_id += 1
            self.predictive_analytics[analysis_id] = {
                "name": name,
                "model_id": model_id,
                "results": results,
                "date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
            self._log_activity("analysis_run", {
                "analysis_id": analysis_id,
                "name": name,
                "model_id": model_id
            })
            return f"Predictive Analysis '{name}' run with ID: {analysis_id}"
        return f"Model ID {model_id} not found."

    # --- Automated Dashboards ---
    def create_dashboard(self, name: str, metrics: List[str], data_sources: List[str], update_frequency: str) -> str:
        """Create an automated compliance dashboard."""
        dashboard_id = f"DASH{self.next_dashboard_id}"
        self.next_dashboard_id += 1
        self.dashboards[dashboard_id] = Dashboard(
            name=name,
            metrics=metrics,
            data_sources=data_sources,
            update_frequency=update_frequency
        )
        self._log_activity("dashboard_created", {
            "dashboard_id": dashboard_id,
            "name": name,
            "metrics": metrics
        })
        return f"Dashboard '{name}' created with ID: {dashboard_id}"

    def update_dashboard(self, dashboard_id: str, new_metrics: List[str]) -> str:
        """Update the metrics in a dashboard."""
        if dashboard_id in self.dashboards:
            self.dashboards[dashboard_id].metrics.extend(new_metrics)
            self._log_activity("dashboard_updated", {
                "dashboard_id": dashboard_id,
                "new_metrics": new_metrics
            })
            return f"Dashboard {dashboard_id} updated with new metrics: {new_metrics}"
        return f"Dashboard ID {dashboard_id} not found."

    # --- International Laws Tracking ---
    def add_international_law(self, name: str, region: str, category: str, impact: str) -> str:
        """Add a new international law impacting marketing, sales, or data flows."""
        law_id = f"LAW{self.next_law_id}"
        self.next_law_id += 1
        self.international_laws[law_id] = {
            "name": name,
            "region": region,
            "category": category,
            "impact": impact,
            "compliance_status": "Not Assessed"
        }
        self._log_activity("law_added", {
            "law_id": law_id,
            "name": name,
            "region": region
        })
        return f"International Law '{name}' added with ID: {law_id}"

    def update_law_compliance(self, law_id: str, status: str) -> str:
        """Update the compliance status of an international law."""
        if law_id in self.international_laws:
            self.international_laws[law_id]["compliance_status"] = status
            self._log_activity("law_compliance_updated", {
                "law_id": law_id,
                "status": status
            })
            return f"Compliance status for Law {law_id} updated to: {status}"
        return f"Law ID {law_id} not found."

    # --- Policy Management ---
    def draft_policy(self, title: str, category: str, requirements: List[str], enforcement_date: str) -> str:
        """Draft a new compliance policy."""
        policy_id = f"POL{self.next_policy_id}"
        self.next_policy_id += 1
        self.policies[policy_id] = Policy(
            title=title,
            category=category,
            requirements=requirements,
            enforcement_date=enforcement_date,
            status="Draft"
        )
        self._log_activity("policy_drafted", {
            "policy_id": policy_id,
            "title": title,
            "category": category
        })
        return f"Policy '{title}' drafted with ID: {policy_id}"

    def enforce_policy(self, policy_id: str) -> str:
        """Enforce a compliance policy."""
        if policy_id in self.policies:
            self.policies[policy_id].status = "Active"
            self._log_activity("policy_enforced", {"policy_id": policy_id})
            return f"Policy {policy_id} enforced."
        return f"Policy ID {policy_id} not found."

    def retire_policy(self, policy_id: str) -> str:
        """Retire an outdated policy."""
        if policy_id in self.policies:
            self.policies[policy_id].status = "Retired"
            self._log_activity("policy_retired", {"policy_id": policy_id})
            return f"Policy {policy_id} retired."
        return f"Policy ID {policy_id} not found."

    # --- Vendor Oversight ---
    def add_vendor(self, name: str, category: str, risk_level: str = "Medium") -> str:
        """Add a new vendor for oversight."""
        vendor_id = f"VEND{self.next_vendor_id}"
        self.next_vendor_id += 1
        self.vendors[vendor_id] = {
            "name": name,
            "category": category,
            "compliance_status": "Not Assessed",
            "risk_level": risk_level
        }
        self._log_activity("vendor_added", {
            "vendor_id": vendor_id,
            "name": name,
            "category": category
        })
        return f"Vendor '{name}' added with ID: {vendor_id}"

    def update_vendor_compliance(self, vendor_id: str, status: str) -> str:
        """Update the compliance status of a vendor."""
        if vendor_id in self.vendors:
            self.vendors[vendor_id]["compliance_status"] = status
            self._log_activity("vendor_compliance_updated", {
                "vendor_id": vendor_id,
                "status": status
            })
            return f"Compliance status for Vendor {vendor_id} updated to: {status}"
        return f"Vendor ID {vendor_id} not found."

    # --- Data Flow Monitoring ---
    def add_data_flow(self, source: str, destination: str, data_type: str) -> str:
        """Add a new data flow for compliance monitoring."""
        flow_id = f"FLOW{self.next_flow_id}"
        self.next_flow_id += 1
        self.data_flows[flow_id] = {
            "source": source,
            "destination": destination,
            "data_type": data_type,
            "compliance_status": "Not Assessed"
        }
        self._log_activity("data_flow_added", {
            "flow_id": flow_id,
            "source": source,
            "destination": destination
        })
        return f"Data Flow from {source} to {destination} added with ID: {flow_id}"

    def update_flow_compliance(self, flow_id: str, status: str) -> str:
        """Update the compliance status of a data flow."""
        if flow_id in self.data_flows:
            self.data_flows[flow_id]["compliance_status"] = status
            self._log_activity("flow_compliance_updated", {
                "flow_id": flow_id,
                "status": status
            })
            return f"Compliance status for Data Flow {flow_id} updated to: {status}"
        return f"Flow ID {flow_id} not found."

    # --- Audit Logging ---
    def _log_activity(self, action: str, details: Dict) -> None:
        """Log an activity to the audit trail."""
        log_entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "action": action,
            "details": details
        }
        self.audit_logs.append(log_entry)

    def get_audit_logs(self) -> List[Dict]:
        """Retrieve all audit logs."""
        return self.audit_logs

    # --- Reporting ---
    def generate_risk_report(self) -> Dict:
        """Generate a report on detected risks and trends."""
        report = {
            "total_risks": len(self.risks),
            "risks_by_category": self._count_risks_by_category(),
            "risks_by_severity": self._count_risks_by_severity(),
            "avg_risk_score": self._calculate_avg_risk_score(),
            "risks": [
                {
                    "risk_id": risk_id,
                    "description": risk.description,
                    "category": risk.category,
                    "severity": risk.severity,
                    "risk_score": risk.likelihood * risk.impact,
                    "mitigation": risk.mitigation
                }
                for risk_id, risk in self.risks.items()
            ]
        }
        return report

    def _count_risks_by_category(self) -> Dict:
        """Count risks by category."""
        categories = {}
        for risk in self.risks.values():
            if risk.category not in categories:
                categories[risk.category] = 0
            categories[risk.category] += 1
        return categories

    def _count_risks_by_severity(self) -> Dict:
        """Count risks by severity."""
        severities = {}
        for risk in self.risks.values():
            if risk.severity not in severities:
                severities[risk.severity] = 0
            severities[risk.severity] += 1
        return severities

    def _calculate_avg_risk_score(self) -> float:
        """Calculate the average risk score."""
        if not self.risks:
            return 0.0
        total = sum(risk.likelihood * risk.impact for risk in self.risks.values())
        return total / len(self.risks)

    def generate_campaign_report(self) -> Dict:
        """Generate a report on multi-channel campaigns and their compliance status."""
        report = {
            "total_campaigns": len(self.campaigns),
            "campaigns_by_status": self._count_campaigns_by_status(),
            "campaigns_by_market": self._count_campaigns_by_market(),
            "avg_risks_per_campaign": self._calculate_avg_risks_per_campaign(),
            "campaigns": [
                {
                    "campaign_id": camp_id,
                    "name": campaign.name,
                    "channels": campaign.channels,
                    "markets": campaign.markets,
                    "status": campaign.status,
                    "start_date": campaign.start_date,
                    "end_date": campaign.end_date,
                    "risks": [self.risks[risk_id].__dict__ for risk_id in getattr(campaign, "risks", [])]
                }
                for camp_id, campaign in self.campaigns.items()
            ]
        }
        return report

    def _count_campaigns_by_status(self) -> Dict:
        """Count campaigns by status."""
        statuses = {}
        for campaign in self.campaigns.values():
            if campaign.status not in statuses:
                statuses[campaign.status] = 0
            statuses[campaign.status] += 1
        return statuses

    def _count_campaigns_by_market(self) -> Dict:
        """Count campaigns by market."""
        markets = {}
        for campaign in self.campaigns.values():
            for market in campaign.markets:
                if market not in markets:
                    markets[market] = 0
                markets[market] += 1
        return markets

    def _calculate_avg_risks_per_campaign(self) -> float:
        """Calculate the average number of risks per campaign."""
        total_risks = sum(len(getattr(campaign, "risks", [])) for campaign in self.campaigns.values())
        return total_risks / len(self.campaigns) if self.campaigns else 0.0

    def generate_compliance_report(self) -> Dict:
        """Generate a report on compliance with international laws and policies."""
        report = {
            "total_laws": len(self.international_laws),
            "laws_by_region": self._count_laws_by_region(),
            "laws_by_category": self._count_laws_by_category(),
            "compliance_status": self._count_laws_by_compliance(),
            "total_policies": len(self.policies),
            "policies_by_category": self._count_policies_by_category(),
            "policy_statuses": self._count_policies_by_status()
        }
        return report

    def _count_laws_by_region(self) -> Dict:
        """Count international laws by region."""
        regions = {}
        for law in self.international_laws.values():
            if law["region"] not in regions:
                regions[law["region"]] = 0
            regions[law["region"]] += 1
        return regions

    def _count_laws_by_category(self) -> Dict:
        """Count international laws by category."""
        categories = {}
        for law in self.international_laws.values():
            if law["category"] not in categories:
                categories[law["category"]] = 0
            categories[law["category"]] += 1
        return categories

    def _count_laws_by_compliance(self) -> Dict:
        """Count international laws by compliance status."""
        statuses = {}
        for law in self.international_laws.values():
            if law["compliance_status"] not in statuses:
                statuses[law["compliance_status"]] = 0
            statuses[law["compliance_status"]] += 1
        return statuses

    def _count_policies_by_category(self) -> Dict:
        """Count policies by category."""
        categories = {}
        for policy in self.policies.values():
            if policy.category not in categories:
                categories[policy.category] = 0
            categories[policy.category] += 1
        return categories

    def _count_policies_by_status(self) -> Dict:
        """Count policies by status."""
        statuses = {}
        for policy in self.policies.values():
            if policy.status not in statuses:
                statuses[policy.status] = 0
            statuses[policy.status] += 1
        return statuses

    def generate_dashboard_report(self) -> Dict:
        """Generate a report on automated dashboards and their metrics."""
        report = {
            "total_dashboards": len(self.dashboards),
            "dashboards": [
                {
                    "dashboard_id": dash_id,
                    "name": dashboard.name,
                    "metrics": dashboard.metrics,
                    "data_sources": dashboard.data_sources,
                    "update_frequency": dashboard.update_frequency
                }
                for dash_id, dashboard in self.dashboards.items()
            ]
        }
        return report

    def generate_vendor_report(self) -> Dict:
        """Generate a report on vendor oversight and compliance."""
        report = {
            "total_vendors": len(self.vendors),
            "vendors_by_category": self._count_vendors_by_category(),
            "vendors_by_risk": self._count_vendors_by_risk(),
            "vendors_by_compliance": self._count_vendors_by_compliance(),
            "vendors": [
                {
                    "vendor_id": vend_id,
                    "name": vendor["name"],
                    "category": vendor["category"],
                    "risk_level": vendor["risk_level"],
                    "compliance_status": vendor["compliance_status"]
                }
                for vend_id, vendor in self.vendors.items()
            ]
        }
        return report

    def _count_vendors_by_category(self) -> Dict:
        """Count vendors by category."""
        categories = {}
        for vendor in self.vendors.values():
            if vendor["category"] not in categories:
                categories[vendor["category"]] = 0
            categories[vendor["category"]] += 1
        return categories

    def _count_vendors_by_risk(self) -> Dict:
        """Count vendors by risk level."""
        risks = {}
        for vendor in self.vendors.values():
            if vendor["risk_level"] not in risks:
                risks[vendor["risk_level"]] = 0
            risks[vendor["risk_level"]] += 1
        return risks

    def _count_vendors_by_compliance(self) -> Dict:
        """Count vendors by compliance status."""
        statuses = {}
        for vendor in self.vendors.values():
            if vendor["compliance_status"] not in statuses:
                statuses[vendor["compliance_status"]] = 0
            statuses[vendor["compliance_status"]] += 1
        return statuses

    def generate_data_flow_report(self) -> Dict:
        """Generate a report on data flows and their compliance."""
        report = {
            "total_flows": len(self.data_flows),
            "flows_by_data_type": self._count_flows_by_data_type(),
            "flows_by_compliance": self._count_flows_by_compliance(),
            "flows": [
                {
                    "flow_id": flow_id,
                    "source": flow["source"],
                    "destination": flow["destination"],
                    "data_type": flow["data_type"],
                    "compliance_status": flow["compliance_status"]
                }
                for flow_id, flow in self.data_flows.items()
            ]
        }
        return report

    def _count_flows_by_data_type(self) -> Dict:
        """Count data flows by data type."""
        types = {}
        for flow in self.data_flows.values():
            if flow["data_type"] not in types:
                types[flow["data_type"]] = 0
            types[flow["data_type"]] += 1
        return types

    def _count_flows_by_compliance(self) -> Dict:
        """Count data flows by compliance status."""
        statuses = {}
        for flow in self.data_flows.values():
            if flow["compliance_status"] not in statuses:
                statuses[flow["compliance_status"]] = 0
            statuses[flow["compliance_status"]] += 1
        return statuses

# --- Example Usage ---
if __name__ == "__main__":
    att = ATTComplianceAnalyst()

    # Create multi-channel campaigns
    print("=== Campaign Management ===")
    print(att.create_campaign("Summer Promotion", ["Email", "Social Media", "SMS"], ["US", "EU"], "2024-06-01", "2024-08-31"))
    print(att.create_campaign("New Product Launch", ["TV", "Digital"], ["US", "APAC"], "2024-07-15", "2024-09-30"))
    print(att.submit_campaign_for_review("CAMP1"))
    print(att.approve_campaign("CAMP1", "Compliance Team"))

    # Detect and mitigate risks
    print("\n=== Risk Detection ===")
    print(att.detect_risk("Non-compliance with GDPR in EU emails", "Regulatory", "High", 4, 5, "CAMP1"))
    print(att.detect_risk("Potential reputational damage from SMS content", "Reputational", "Medium", 3, 4, "CAMP1"))
    print(att.add_mitigation("RISK1", "Implement GDPR-compliant email templates"))
    print(att.add_mitigation("RISK2", "Review SMS content with legal team"))

    # Build statistical models and run predictive analytics
    print("\n=== Statistical Modeling and Predictive Analytics ===")
    print(att.build_statistical_model("Campaign Risk Model", "Logistic Regression", {"features": ["channel", "market", "content_type"]}))
    print(att.train_model("MODEL1", 92.5))  # 92.5% accuracy
    print(att.run_predictive_analysis("Campaign Risk Prediction", "MODEL1", {"high_risk_campaigns": ["CAMP2"], "low_risk_campaigns": ["CAMP1"]}))

    # Create automated dashboards
    print("\n=== Automated Dashboards ===")
    print(att.create_dashboard("Compliance Dashboard", ["Risk Count", "Campaign Approval Rate"], ["SQL", "Python"], "Daily"))
    print(att.update_dashboard("DASH1", ["Vendor Compliance Rate", "Data Flow Compliance"]))

    # Track international laws
    print("\n=== International Laws Tracking ===")
    print(att.add_international_law("GDPR", "EU", "Data Privacy", "High"))
    print(att.add_international_law("CAN-SPAM Act", "US", "Marketing", "Medium"))
    print(att.update_law_compliance("LAW1", "Compliant"))

    # Draft and enforce policies
    print("\n=== Policy Management ===")
    print(att.draft_policy("Digital Marketing Policy", "Digital Marketing", ["GDPR compliance", "Content approval"], "2024-06-01"))
    print(att.draft_policy("Data Use Policy", "Data Use", ["Customer data protection", "Third-party sharing"], "2024-06-01"))
    print(att.enforce_policy("POL1"))

    # Manage vendor oversight
    print("\n=== Vendor Oversight ===")
    print(att.add_vendor("Marketing Agency A", "Marketing", "High"))
    print(att.add_vendor("Data Analytics Firm", "Data Processing", "Medium"))
    print(att.update_vendor_compliance("VEND1", "Compliant"))

    # Monitor data flows
    print("\n=== Data Flow Monitoring ===")
    print(att.add_data_flow("CRM System", "Marketing Agency A", "Customer Data"))
    print(att.add_data_flow("Mobile App", "Data Analytics Firm", "User Behavior Data"))
    print(att.update_flow_compliance("FLOW1", "Compliant"))

    # Generate reports
    print("\n=== Risk Report ===")
    risk_report = att.generate_risk_report()
    for key, value in risk_report.items():
        print(f"{key}: {value}")

    print("\n=== Campaign Report ===")
    campaign_report = att.generate_campaign_report()
    for key, value in campaign_report.items():
        print(f"{key}: {value}")

    print("\n=== Compliance Report ===")
    compliance_report = att.generate_compliance_report()
    for key, value in compliance_report.items():
        print(f"{key}: {value}")

    print("\n=== Dashboard Report ===")
    dashboard_report = att.generate_dashboard_report()
    for key, value in dashboard_report.items():
        print(f"{key}: {value}")

    print("\n=== Vendor Report ===")
    vendor_report = att.generate_vendor_report()
    for key, value in vendor_report.items():
        print(f"{key}: {value}")

    print("\n=== Data Flow Report ===")
    data_flow_report = att.generate_data_flow_report()
    for key, value in data_flow_report.items():
        print(f"{key}: {value}")
