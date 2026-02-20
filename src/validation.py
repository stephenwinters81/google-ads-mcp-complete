"""Input validation and sanitization for Google Ads MCP server.

Prevents GAQL injection, path traversal, and other input-based attacks.
"""

import re
from pathlib import Path
from typing import List, Optional, Set


class ValidationError(ValueError):
    """Raised when input validation fails."""
    pass


# --- ID Validators ---

def validate_customer_id(customer_id: str) -> str:
    """Validate and normalize a Google Ads customer ID. Returns digits only."""
    cleaned = str(customer_id).replace("-", "").strip()
    if not re.fullmatch(r"\d{1,10}", cleaned):
        raise ValidationError(
            f"Invalid customer ID: must be a numeric string (up to 10 digits), got {customer_id!r}"
        )
    return cleaned


def validate_numeric_id(value: str, field_name: str = "ID") -> str:
    """Validate that a value is a strictly numeric ID string."""
    cleaned = str(value).strip()
    if not re.fullmatch(r"\d+", cleaned):
        raise ValidationError(
            f"Invalid {field_name}: must be numeric, got {value!r}"
        )
    return cleaned


# --- Enum Validators ---

CAMPAIGN_STATUSES = {"ENABLED", "PAUSED", "REMOVED"}
AD_GROUP_STATUSES = {"ENABLED", "PAUSED", "REMOVED"}
AD_STATUSES = {"ENABLED", "PAUSED", "REMOVED"}
KEYWORD_STATUSES = {"ENABLED", "PAUSED", "REMOVED"}

CAMPAIGN_TYPES = {
    "SEARCH", "DISPLAY", "SHOPPING", "VIDEO", "MULTI_CHANNEL",
    "LOCAL", "SMART", "PERFORMANCE_MAX", "DEMAND_GEN",
    "LOCAL_SERVICES", "TRAVEL", "UNKNOWN", "UNSPECIFIED",
}

KEYWORD_MATCH_TYPES = {"EXACT", "PHRASE", "BROAD"}

AD_TYPES = {
    "RESPONSIVE_SEARCH_AD", "EXPANDED_TEXT_AD", "RESPONSIVE_DISPLAY_AD",
    "CALL_AD", "IMAGE_AD", "VIDEO_AD", "APP_AD", "SHOPPING_PRODUCT_AD",
    "SHOPPING_SMART_AD", "TEXT_AD", "EXPANDED_DYNAMIC_SEARCH_AD",
    "HOTEL_AD", "APP_ENGAGEMENT_AD", "LEGACY_RESPONSIVE_DISPLAY_AD",
    "SMART_CAMPAIGN_AD", "DISCOVERY_MULTI_ASSET_AD",
    "DISCOVERY_CAROUSEL_AD", "TRAVEL_AD", "DEMAND_GEN_MULTI_ASSET_AD",
    "DEMAND_GEN_CAROUSEL_AD", "DEMAND_GEN_VIDEO_RESPONSIVE_AD",
    "DEMAND_GEN_PRODUCT_AD",
}

AUDIENCE_TYPES = {
    "REMARKETING", "SIMILAR", "CUSTOM_INTENT", "CUSTOM_AFFINITY",
    "BASIC_USER_LIST", "LOGICAL_USER_LIST", "RULE_BASED",
    "CRM_BASED", "LOOKALIKE",
}

EXTENSION_TYPES = {
    "SITELINK", "CALL", "CALLOUT", "STRUCTURED_SNIPPET",
    "PRICE", "PROMOTION", "APP", "LEAD_FORM", "IMAGE",
    "HOTEL_CALLOUT", "LOCATION",
}

LOCATION_TYPES = {
    "MOST_SPECIFIC", "LOCATION_OF_PRESENCE",
    "AREA_OF_INTEREST", "GEO_TARGET",
    "COUNTRY_AND_REGION",
}

ASSET_TYPES = {
    "IMAGE", "TEXT", "LEAD_FORM", "BOOK_ON_GOOGLE", "PROMOTION",
    "CALLOUT", "STRUCTURED_SNIPPET", "SITELINK", "PAGE_FEED",
    "DYNAMIC_EDUCATION", "MOBILE_APP", "HOTEL_CALLOUT",
    "CALL", "PRICE", "CALL_TO_ACTION", "DYNAMIC_REAL_ESTATE",
    "DYNAMIC_CUSTOM", "DYNAMIC_HOTELS_AND_RENTALS", "DYNAMIC_FLIGHTS",
    "DYNAMIC_TRAVEL", "DYNAMIC_LOCAL", "DYNAMIC_JOBS",
    "LOCATION", "HOTEL_PROPERTY", "MEDIA_BUNDLE", "YOUTUBE_VIDEO",
    "DISCOVERY_CAROUSEL_CARD", "DEMAND_GEN_CAROUSEL_CARD",
}

BIDDING_STRATEGY_TYPES = {
    "MANUAL_CPC", "MANUAL_CPM", "MANUAL_CPV",
    "MAXIMIZE_CLICKS", "MAXIMIZE_CONVERSIONS", "MAXIMIZE_CONVERSION_VALUE",
    "TARGET_CPA", "TARGET_ROAS", "TARGET_SPEND",
    "TARGET_IMPRESSION_SHARE", "ENHANCED_CPC",
    "COMMISSION", "PERCENT_CPC",
}

DATE_RANGES = {
    "TODAY", "YESTERDAY", "LAST_7_DAYS", "LAST_14_DAYS",
    "LAST_30_DAYS", "LAST_BUSINESS_WEEK", "THIS_MONTH",
    "LAST_MONTH", "THIS_WEEK_MON_TODAY", "THIS_WEEK_SUN_TODAY",
    "LAST_WEEK_MON_SUN", "LAST_WEEK_SUN_SAT",
    "ALL_TIME",
}


def validate_enum(value: str, allowed: Set[str], field_name: str = "value") -> str:
    """Validate that a string value is in the allowed set (case-insensitive)."""
    upper = str(value).strip().upper()
    if upper not in allowed:
        allowed_str = ", ".join(sorted(allowed))
        raise ValidationError(
            f"Invalid {field_name}: {value!r}. Must be one of: {allowed_str}"
        )
    return upper


# --- GAQL String Sanitization ---

def sanitize_gaql_string(value: str) -> str:
    """Escape a string value for safe use in GAQL single-quoted literals."""
    value = str(value)
    value = value.replace("\\", "\\\\")
    value = value.replace("'", "\\'")
    value = value.replace("\n", " ").replace("\r", " ")
    return value


# --- Date Range Validation ---

_CUSTOM_DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def validate_date_range(date_range: str) -> str:
    """Validate a GAQL date range value."""
    cleaned = str(date_range).strip()
    upper = cleaned.upper()

    if upper in DATE_RANGES:
        return upper

    parts = cleaned.split(",")
    for part in parts:
        part = part.strip()
        if part and not _CUSTOM_DATE_PATTERN.match(part):
            raise ValidationError(
                f"Invalid date range: {date_range!r}. Must be a predefined range "
                f"({', '.join(sorted(DATE_RANGES))}) or YYYY-MM-DD format."
            )

    return cleaned


# --- Metrics Validation ---

VALID_METRICS = {
    "impressions", "clicks", "cost_micros", "conversions",
    "conversions_value", "all_conversions", "all_conversions_value",
    "ctr", "average_cpc", "average_cpm", "average_cpv",
    "average_cost", "cost_per_conversion", "cost_per_all_conversions",
    "interaction_rate", "interactions", "view_through_conversions",
    "video_views", "video_view_rate", "video_quartile_p25_rate",
    "video_quartile_p50_rate", "video_quartile_p75_rate",
    "video_quartile_p100_rate", "search_impression_share",
    "search_rank_lost_impression_share", "search_budget_lost_impression_share",
    "content_impression_share", "content_rank_lost_impression_share",
    "content_budget_lost_impression_share", "search_exact_match_impression_share",
    "absolute_top_impression_percentage", "top_impression_percentage",
    "search_absolute_top_impression_share", "search_top_impression_share",
    "bounce_rate", "phone_calls", "phone_impressions", "phone_through_rate",
    "average_page_views", "average_time_on_site", "percent_new_visitors",
    "cross_device_conversions", "engagement_rate", "engagements",
    "active_view_cpm", "active_view_ctr", "active_view_impressions",
    "active_view_measurability", "active_view_measurable_cost_micros",
    "active_view_measurable_impressions", "active_view_viewability",
    "gmail_forwards", "gmail_saves", "gmail_secondary_clicks",
    "optimization_score_uplift", "optimization_score_url",
    "historical_creative_quality_score", "historical_landing_page_quality_score",
    "historical_search_predicted_ctr", "historical_quality_score",
    "value_per_all_conversions", "value_per_conversion",
    "current_model_attributed_conversions",
    "current_model_attributed_conversions_value",
    "conversions_by_conversion_date", "conversions_value_by_conversion_date",
    "sk_ad_network_conversions",
}


def validate_metric(metric: str) -> str:
    """Validate a single metric name against known Google Ads metrics."""
    cleaned = str(metric).strip().lower()
    if not re.fullmatch(r"[a-z][a-z0-9_]*", cleaned):
        raise ValidationError(
            f"Invalid metric name format: {metric!r}. Must contain only letters, digits, and underscores."
        )
    if cleaned not in VALID_METRICS:
        raise ValidationError(
            f"Unknown metric: {metric!r}. Use a valid Google Ads metric name."
        )
    return cleaned


def validate_metrics(metrics: List[str]) -> List[str]:
    """Validate a list of metric names."""
    return [validate_metric(m) for m in metrics]


# --- Numeric Value Validation ---

def validate_positive_number(value, field_name: str = "value") -> float:
    """Validate that a value is a positive number."""
    try:
        num = float(value)
    except (TypeError, ValueError):
        raise ValidationError(f"Invalid {field_name}: must be a number, got {value!r}")
    if num < 0:
        raise ValidationError(f"Invalid {field_name}: must be non-negative, got {num}")
    return num


# --- GAQL Query Validation (for raw query tool) ---

_GAQL_MUTATION_KEYWORDS = re.compile(
    r"\b(CREATE|UPDATE|REMOVE|MUTATE)\b", re.IGNORECASE
)

MAX_GAQL_RESULTS = 10000


def validate_gaql_query(query: str) -> str:
    """Validate a raw GAQL query to ensure it's read-only and has a LIMIT."""
    cleaned = str(query).strip()

    if not cleaned.upper().startswith("SELECT"):
        raise ValidationError("GAQL query must start with SELECT")

    if _GAQL_MUTATION_KEYWORDS.search(cleaned):
        raise ValidationError("GAQL query must be read-only (no CREATE/UPDATE/REMOVE/MUTATE)")

    if "LIMIT" not in cleaned.upper():
        cleaned += f" LIMIT {MAX_GAQL_RESULTS}"

    return cleaned


# --- File Path Validation ---

ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}


def validate_image_path(path: str, allowed_dirs: Optional[List[str]] = None) -> Path:
    """Validate a file path for image upload."""
    resolved = Path(path).resolve()

    if resolved.suffix.lower() not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            f"Invalid image file type: {resolved.suffix}. "
            f"Allowed: {', '.join(sorted(ALLOWED_IMAGE_EXTENSIONS))}"
        )

    if allowed_dirs:
        if not any(str(resolved).startswith(str(Path(d).resolve())) for d in allowed_dirs):
            raise ValidationError(
                f"File path {path!r} is outside allowed directories"
            )

    if not resolved.is_file():
        raise ValidationError(f"Image file not found: {path}")

    return resolved
