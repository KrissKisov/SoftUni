from typing import List
from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    valid_influencer_types = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    valid_campaign_types = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):

        try:
            influencer = self.valid_influencer_types[influencer_type](username, followers, engagement_rate)
        except KeyError:
            return f"{influencer_type} is not an allowed influencer type."

        if next((i for i in self.influencers if i.username == username), None):
            return f"{username} is already registered."

        self.influencers.append(influencer)

        return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):

        if next((c for c in self.campaigns if c.campaign_id == campaign_id), None):
            return f"Campaign ID {campaign_id} has already been created."

        try:
            campaign = self.valid_campaign_types[campaign_type](campaign_id, brand, required_engagement)
        except KeyError:
            return f"{campaign_type} is not a valid campaign type."

        self.campaigns.append(campaign)

        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):

        influencer = next((i for i in self.influencers if i.username == influencer_username), None)
        campaign = next((c for c in self.campaigns if c.campaign_id == campaign_id), None)

        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' "
                    f"does not meet the eligibility criteria for the campaign with ID {campaign_id}.")

        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)

            return (f"Influencer '{influencer_username}' "
                    f"has successfully participated in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        result = {}

        for c in self.campaigns:
            if c.approved_influencers:
                for i in c.approved_influencers:
                    if c not in result:
                        result[c] = 0
                    result[c] += i.reached_followers(c.__class__.__name__)

        return result

    def influencer_campaign_report(self, username: str):
        influencer = next(i for i in self.influencers if i.username == username)

        if not influencer.campaigns_participated:
            return f"{username} has not participated in any campaigns."

        message = [f"{influencer.__class__.__name__} :) {username} :) participated in the following campaigns:"]

        for c in influencer.campaigns_participated:
            message.append(f"  - Campaign ID: {c.campaign_id}, Brand: {c.brand}, "
                           f"Reached followers: {influencer.reached_followers(c.__class__.__name__)}")

        return "\n".join(message)

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.campaigns, key=lambda sc: (len(sc.approved_influencers), -sc.budget))

        result = ["$$ Campaign Statistics $$"]

        for c in sorted_campaigns:
            result.append(f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
                          f"Total budget: ${c.budget :.2f}, "
                          f"Total reached followers: {sum(i.reached_followers(c.__class__.__name__) for i in c.approved_influencers)}")

        return "\n".join(result)
