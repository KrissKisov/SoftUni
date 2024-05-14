from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)
        self.initial_payment_percentage = 0.85

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * self.initial_payment_percentage

        return float(payment)

    def reached_followers(self, campaign_type: str):

        if campaign_type == "HighBudgetCampaign":
            return int(self.followers * self.engagement_rate * 1.5)

        if campaign_type == "LowBudgetCampaign":
            return int(self.followers * self.engagement_rate * 0.8)
