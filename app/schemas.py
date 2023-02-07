from datetime import datetime
from typing import List
from pydantic import BaseModel


class TestBaseSchema(BaseModel):
    id: str | None = None
    name: str
    description: str
    category: str
    published: bool = False
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class UserBaseSchema(BaseModel):
    id: str | None = None
    first_name: str
    last_name: str
    email: str
    createdAt: datetime | None = None
    updatedAt: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class CampaignSchema(BaseModel):
    campaing_id: int
    agency: str
    campaign_name: str
    client: str
    created_by: str
    modified_by: str
    modified_date: str

class AudienceSchema(BaseModel): 
    audience_id: int

class DayPartRecurringDaySchema(BaseModel): 
    day_part_recurring_day_id: int

class DayPartRangeDaySchema(BaseModel): 
    day_part_range_day_id: int

class FrequencyCappingSchema(BaseModel): 
    frequency_capping_id: int

class MetaDataSchema(BaseModel): 
    metadata_id: int
    type: str

class MetDataDmaSchema(BaseModel): 
    metadata_dma_id: int
    metadata_id: int
    dma_id: str

class GeoSchema(BaseModel): 
    geo_id: int
    included: bool=False

class GeoMetadataIDSchema(BaseModel): 
    geo_metadata_id: int
    geo_id: int
    metadata_id: int

class GeoZipCodeSchema(BaseModel): 
    geo_zipcode_id: int
    geo_id: int
    zipcode: str

class HaitusDaySchema(BaseModel): 
    haitus_day_id: int

class InventorySourceSchema(BaseModel): 
    inventory_source_id: int
    name: str
    type: str

class NetworkSchema(BaseModel): 
    network_id: int
    included: bool=False
    network_ids = list[str]

class PlatformSchema(BaseModel): 
    platform_id: int
    platform_value: str

class SemgmentSchema(BaseModel): 
    segment_id: int

class TemplateSchema(BaseModel): 
    template_id: int
    tenant_id: str

class TemplateExcludedSchema(BaseModel): 
    template_exluded_id: int
    template_id: int
    excluded: str


class TemplateIncludedSchema(BaseModel): 
    template_inluded_id: int
    template_id: int
    included: str

class ProposalSchema(BaseModel): 
    proposal_id: int
    partition_id: str
    sort_id: str
    addressable: bool = False
    cpm: int
    created_by: str
    created_date: str
    end_date: str
    gross_budget: int
    group_id: str
    line_of_business: str
    max_avails: bool = False
    modified_by: str
    modified_date: str
    name: str
    non_guaranteed: bool
    pacing: str
    priority: int
    salesforce_id: str
    start_date: str

class ProposalAudienceSchema(BaseModel): 
    proposal_audience_id: int
    proposal_id: int
    audience_id: int

class ProposalDayPartRecurringDaySchema(BaseModel): 
    proposal_day_part_recurring_day_id: int
    proposal_id: int
    day_part_recurring_days_id: int

class ProposalDayPartRangeDaySchema(BaseModel): 
    proposal_day_part_range_day_id: int
    proposal_id:int
    day_part_range_day_id: int

class ProposalFrequencyCappingSchema(BaseModel): 
    proposal_frequency_capping_id: int
    proposal_id: int
    frequency_capping_id: int

class ProposalGeoSchema(BaseModel): 
    proposal_geo_id: int
    proposal_id: int
    geo_id: int

class ProposalHaitusDaySchema(BaseModel): 
    proposal_haitus_day_id: int
    proposal_id: int
    haitus_day_id: int

class ProposalInventorySourceSchema(BaseModel): 
    proposal_inventory_source_id: int
    proposal_id: int
    inventory_source_id: int

class ProposalNetworkSchema(BaseModel): 
    proposal_network_id: int
    proposal_id: int
    network_id: int

class ProposalPlatformSchema(BaseModel): 
    proposal_platform_id: int
    proposal_id: int
    plaform_id: int

class ProposalSegmentSchema(BaseModel): 
    proposal_segment_id: int
    proposal_id: int
    segment_id: int


class ProposalTemplateSchema(BaseModel): 
    proposal_template_id: int
    proposal_id: int
    template_id: int


class YieldSchema(BaseModel): 
    yield_id: int
    proposal_id: int
    availables_to_purchase: int
    gross_available: int
    net_availables: int

class ProposalRecommendationSchema(BaseModel): 
    proposal_recommendation_id: int
    proposal_id:int
    transaction_id:int
    job_status:str
    type:str
    created_date:str
    yield_id:int


class ListTestResponse(BaseModel):
    status: str
    tests: List[TestBaseSchema]


class ListUserResponse(BaseModel):
    status: str
    tests: List[UserBaseSchema]
