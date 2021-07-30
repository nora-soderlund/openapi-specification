<!--- This is a generated file, do not edit! -->
<!--- [START maps_http_parameters_placenearbysearch] -->
<h2 id="required-parameters">Required parameters</h2>

-   <h3 id="location">location</h3>

    The point around which to retrieve place information. This must be specified as `latitude,longitude`.

<h2 id="optional-parameters">Optional parameters</h2>

-   <h3 id="fields">fields</h3>

    Use the fields parameter to specify a comma-separated list of place data types to return. For example: `fields=formatted_address,name,geometry`. Use a forward slash when specifying compound values. For example: `opening_hours/open_now`.

    Fields are divided into three billing categories: Basic, Contact, and Atmosphere. Basic fields are billed at base rate, and incur no additional charges. Contact and Atmosphere fields are billed at a higher rate. See the [pricing sheet](https://cloud.google.com/maps-platform/pricing/sheet/) for more information. Attributions, `html_attributions`, are always returned with every call, regardless of whether the field has been requested.

    **Basic**

    The Basic category includes the following fields: `address_component`, `adr_address`, `business_status`, `formatted_address`, `geometry`, `icon`, `name`, `photo`, `place_id`, `plus_code`, `type`, `url`, `utc_offset`, `vicinity`.

    **Contact**

    The Contact category includes the following fields: `formatted_phone_number`, `international_phone_number`, `opening_hours`, `website`

    **Atmosphere**

    The Atmosphere category includes the following fields: `price_level`, `rating`, `review`, `user_ratings_total`.

    <div class="caution">Caution: Place Search requests and Place Details requests do not return the same fields. Place Search requests return a subset of the fields that are returned by Place Details requests. If the field you want is not returned by Place Search, you can use Place Search to get a place_id, then use that Place ID to make a Place Details request.</div>

-   <h3 id="keyword">keyword</h3>

    A term to be matched against all content that Google has indexed for this place, including but not limited to name, type, and address, as well as customer reviews and other third-party content.

-   <h3 id="language">language</h3>

    The language in which to return results.

    -   See the [list of supported languages](https://developers.google.com/maps/faq#languagesupport). Google often updates the supported languages, so this list may not be exhaustive.
    -   If `language` is not supplied, the API attempts to use the preferred language as specified in the `Accept-Language` header, or the native language of the domain from which the request is sent.
    -   The API does its best to provide a street address that is readable for both the user and locals. To achieve that goal, it returns street addresses in the local language, transliterated to a script readable by the user if necessary, observing the preferred language. All other addresses are returned in the preferred language. Address components are all returned in the same language, which is chosen from the first component.
    -   If a name is not available in the preferred language, the API uses the closest match.
    -   The preferred language has a small influence on the set of results that the API chooses to return, and the order in which they are returned. The geocoder interprets abbreviations differently depending on language, such as the abbreviations for street types, or synonyms that may be valid in one language but not in another. For example, *utca* and *tér* are synonyms for street in Hungarian.

-   <h3 id="maxprice">maxprice</h3>

    Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount indicated by a specific value will vary from region to region.

-   <h3 id="minprice">minprice</h3>

    Restricts results to only those places within the specified range. Valid values range between 0 (most affordable) to 4 (most expensive), inclusive. The exact amount indicated by a specific value will vary from region to region.

-   <h3 id="name">name</h3>

    *Not Recommended* A term to be matched against all content that Google has indexed for this place. Equivalent to `keyword`. The `name` field is no longer restricted to place names. Values in this field are combined with values in the keyword field and passed as part of the same search string. We recommend using only the `keyword` parameter for all search terms.

-   <h3 id="opennow">opennow</h3>

    Returns only those places that are open for business at the time the query is sent. Places that do not specify opening hours in the Google Places database will not be returned if you include this parameter in your query.

-   <h3 id="pagetoken">pagetoken</h3>

    Returns up to 20 results from a previously run search. Setting a `pagetoken` parameter will execute a search with the same parameters used previously — all parameters other than pagetoken will be ignored.

-   <h3 id="radius">radius</h3>

    Defines the distance (in meters) within which to return place results.

-   <h3 id="rankby">rankby</h3>

    Specifies the order in which results are listed. Possible values are:

    -   `prominence` (default). This option sorts results based on their importance. Ranking will favor prominent places within the set radius over nearby places that match but that are less prominent. Prominence can be affected by a place's ranking in Google's index, global popularity, and other factors. When prominence is specified, the `radius` parameter is required.
    -   `distance`. This option biases search results in ascending order by their distance from the specified location. When `distance` is specified, one or more of `keyword`, `name`, or `type` is required.

-   <h3 id="type">type</h3>

    Restricts the results to places matching the specified type. Only one type may be specified (if more than one type is provided, all types following the first entry are ignored). See the list of [supported types](https://developers.google.com/maps/documentation/places/web-service/supported_types).

    <div class="note">Note: Adding both `keyword` and `type` with the same value (`keyword=cafe&type=cafe` or `keyword=parking&type=parking`) can yield `ZERO_RESULTS`.</div>


<p style="text-align: right; font-size: smaller;">Generated from the <a class="gc-analytics-event" data-category="GMP" data-label="openapi-github" href="https://github.com/googlemaps/openapi-specification" title="Google Maps Platform OpenAPI Specification" class="external">OpenAPI specification</a>.
<a class="gc-analytics-event" data-category="GMP" data-label="openapi-github" style="margin-left: 5px;" href="https://github.com/googlemaps/openapi-specification/blob/main/specification/parameters" title="Edit on GitHub"><span class="material-icons">edit</span> Edit</a>
<a class="gc-analytics-event" data-category="GMP" data-label="openapi-github" style="margin-left: 5px;" href="https://github.com/googlemaps/openapi-specification/issues/new?assignees=&labels=type%3A+bug%2C+triage+me&template=bug_report.md&title=[parameters] Bug - /maps/api/place/nearbysearch/json" title="File bug for parameters on GitHub"><span class="material-icons">bug_report</span> Report bug</a>
</p>

<!--- [END maps_http_parameters_placenearbysearch] -->