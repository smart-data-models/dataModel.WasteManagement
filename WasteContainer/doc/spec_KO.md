<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 폐기물 컨테이너    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **폐기물 용기**    
버전: 0.3.0    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `RFID[string]`: RFID 리더의 ID를 제공합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `actuationHours[string]`: 컨테이너에 대한 작동을 수행하기에 적합한 시간  . Model: [openingHours](openingHours)- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.      
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호      
- `alternateName[string]`: 이 항목의 대체 이름  - `annotations[array]`: 항목에 대한 주석  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `binCapacity[number]`: 쓰레기통에 담을 수 있는 쓰레기 양을 기준으로 한 총 용량  . Model: [https://schema.org/Number](https://schema.org/Number)- `binColor[string]`: 쓰레기통의 색상. 폐기물의 종류를 표시하는 데 사용할 수 있습니다. 색상 코딩은 쓰레기통이 위치한 지역에 적용되는 규칙을 따라야 합니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `binFullnessThreshold[number]`: 빈 만함 임계값 수준은 빈 만함 경고 또는 알림이 생성되는 수준(백분율 기준)으로 정의됩니다.  . Model: [https://schema.org/Number](https://schema.org/Number)- `binId[string]`: 폐기물 운반용 쓰레기통의 ID  . Model: [https://schema.org/Text](https://schema.org/Text)- `binLoggedTime[date-time]`: 휴지통의 레벨이 마지막으로 기록된 시간  . Model: [https://schema.org/Text](https://schema.org/Text)- `binMaxLoad[number]`: 쓰레기통에 담을 수 있는 최대 하중(무게)  . Model: [https://schema.org/Number](https://schema.org/Number)- `binRecommendedLoad[number]`: 이 관측에 해당하는 쓰레기통에 담을 수 있는 권장 하중(무게)  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: 컨테이너 적재 중량  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: 컨테이너의 카테고리. Enum:'고정, 지상, 기타, 휴대용, 지하'  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: 제품의 색상  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateLastCleaning[date-time]`: 마지막으로 용기를 청소한 시기.  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastEmptying[date-time]`: 마지막으로 컨테이너를 비운 시점을 나타내는 타임스탬프  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateServiceStarted[date-time]`: 컨테이너가 서비스를 제공하기 시작한 날짜  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: 이 항목에 대한 설명  - `fillingLevel[number]`: 컨테이너의 충전 레벨  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: 엔티티의 고유 식별자  - `image[uri]`: 항목 이미지  . Model: [https://schema.org/URL](https://schema.org/URL)- `isleId[string]`: 컨테이너가 배치된 섬의 식별자(또는 이름)입니다. 이 속성은 `WasteContainerIsle` 유형의 엔티티가 특별히 모델링되지 않을 때 사용해야 합니다. 그렇지 않으면 `refWasteContainerIsle`을 사용해야 합니다.  - `license_plate[string]`: 차량의 번호판 번호를 제공합니다. SameAs: GTFS 실시간 메시지-차량 설명자(https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)의 'license_plate' 필드  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `methaneConcentration[number]`: 용기 내부의 메탄(CH4) 농도  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: 이 항목의 이름  - `nextActuationDeadline[date-time]`: 다음 작동(비우기, 픽업 등)을 수행해야 하는 마감 시간  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `nextCleaningDeadline[date-time]`: 다음 청소 마감일  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `refDevice[array]`: 이 컨테이너를 모니터링하는 데 사용되는 장치에 대한 참조  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerIsle[*]`: 컨테이너가 배치된 섬  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerModel[*]`: 컨테이너 모델  . Model: [http://schema.org/URL](http://schema.org/URL)- `regulation[string]`: 컨테이너가 운영되는 규정  . Model: [http://schema.org/Text](http://schema.org/Text)- `responsible[string]`: 컨테이너에 대한 책임자, 즉 작동(비우기, 수거 등)을 담당하는 주체  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `serialNumber[string]`: 컨테이너의 일련 번호  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `status[string]`: 안전 관점에서 컨테이너의 상태. Enum:'ok , 뚜껑열림 , 떨어뜨림 , 이동 , 파손 , 불타고 있음 , 알 수 없음'.  - `ok`. 컨테이너가 있어야 할 곳에 있고 제대로 서 있습니다. `lidOpen`. 컨테이너의 뚜껑이 열렸고 일정 시간이 지나도 닫히지 않았습니다. 떨어뜨림`. 컨테이너가 어떤 이유로 떨어졌습니다. `moved`. 컨테이너가 원래 위치에서 이동한 후 다시 돌아오지 않았습니다. 파손됨`. 컨테이너가 기물 파손으로 인해 손상되었거나 파손되었습니다. 불타고 있음`. 컨테이너가 타는 중이며 즉각적인 조치가 필요합니다. 알 수 없음`. 컨테이너의 상태를 시스템에서 알 수 없습니다.  - `storedWasteCode[string]`: 대상 규정에 따라 다릅니다. 유럽의 경우 [유럽 폐기물 목록](http://ec.europa.eu/environment/waste/framework/list.htm)을 확인하세요.  . Model: [https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind](https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind)- `storedWasteKind[string]`: 컨테이너에 보관된 폐기물의 종류. 열거형: '유기, 무기, 유리, 기름, 플라스틱, 금속, 종이, 배터리, 전자제품, 유해, 기타'. 또는 전자에 속하지 않는 다른 값.  . Model: [https://schema.org/Text](https://schema.org/Text)- `storedWasteOrigin[string]`: 보관된 폐기물의 출처. 열거형: '가정, 도시, 산업, 건설, 숙박, 농업, 기타'  . Model: [https://schema.org/Text](https://schema.org/Text)- `temperature[number]`: 용기 내부 온도  . Model: [http://schema.org/Number](http://schema.org/Number)- `timeInstant[date-time]`: 페이로드의 타임스탬프입니다. 프로덕션 환경에서는 속성 유형이 `ISO8601` 문자열과 같을 수 있습니다. 이 경우 `DateTime`의 동의어로 간주해야 합니다. 이 속성은 이전 FIWARE 참조 구현과의 하위 호환성을 위해 유지됩니다.  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI 엔티티 유형: WasteContainer여야 합니다.  - `wardId[string]`: 이 관찰에 해당하는 엔티티의 병동 ID  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
WasteContainer:      
  description: A waste container      
  properties:      
    RFID:      
      description: Gives the ID of the RFID reader      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    actuationHours:      
      description: Hours suitable for performing actuations over the container      
      type: string      
      x-ngsi:      
        model: openingHours      
        type: Property      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    annotations:      
      description: Annotations about the item      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binCapacity:      
      description: Total capacity in terms of the volume of waste the bin can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    binColor:      
      description: Color of the bin. Could be used for indicating the type of waste. The color coding should follow the conventions applicable to the geographical area the bins are located      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binFullnessThreshold:      
      description: The fullness threshold level of the bin defined as the level (in terms of percentage) when the bin full alert or notification will be generated      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    binId:      
      description: Id of the waste carrying bin      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binLoggedTime:      
      description: Time when the bin's level was last logged      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    binMaxLoad:      
      description: Maximum load (weight) that the waste bin can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    binRecommendedLoad:      
      description: Recommended load (weight) that the waste bin corresponding to this observation can hold      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    cargoWeight:      
      description: Weight of the container load      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    category:      
      description: 'Container''s category. Enum:'' fixed, ground, other, portable, underground'''      
      items:      
        enum:      
          - fixed      
          - ground      
          - other      
          - portable      
          - underground      
        type: string      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    color:      
      description: The color of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/color      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateLastCleaning:      
      description: 'When the container was cleaned last time. '      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastEmptying:      
      description: Timestamp which represents when the container was emptied last time      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateServiceStarted:      
      description: Date at which the container started giving service      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Date      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    fillingLevel:      
      description: Filling level of the container      
      maximum: 1      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    image:      
      description: An image of the item      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/URL      
        type: Property      
    isleId:      
      description: 'Identifier (or name) of the isle where the container is placed. This attribute should be used when entities of type `WasteContainerIsle` are not being modelled specifically. Otherwise, `refWasteContainerIsle` should be used'      
      type: string      
      x-ngsi:      
        type: Property      
    license_plate:      
      description: "Gives the License Plate number of the vehicle. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)"      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                type: number      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - Point      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              minItems: 2      
              type: array      
            type:      
              enum:      
                - LineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 4      
                type: array      
              type: array      
            type:      
              enum:      
                - Polygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  type: number      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPoint      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    type: number      
                  minItems: 2      
                  type: array      
                minItems: 2      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiLineString      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
          properties:      
            bbox:      
              items:      
                type: number      
              minItems: 4      
              type: array      
            coordinates:      
              items:      
                items:      
                  items:      
                    items:      
                      type: number      
                    minItems: 2      
                    type: array      
                  minItems: 4      
                  type: array      
                type: array      
              type: array      
            type:      
              enum:      
                - MultiPolygon      
              type: string      
          required:      
            - type      
            - coordinates      
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    methaneConcentration:      
      description: Methane (CH4) concentration inside the container      
      minimum: 0      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nextActuationDeadline:      
      description: 'Deadline for next actuation to be performed (emptying, picking up, etc.)'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    nextCleaningDeadline:      
      description: Deadline for next cleaning      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    refDevice:      
      description: Reference to the device(s) used to monitor this container      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      minItems: 1      
      type: array      
      uniqueItems: true      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    refWasteContainerIsle:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Isle where the container is placed      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    refWasteContainerModel:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Container's model      
      x-ngsi:      
        model: http://schema.org/URL      
        type: Relationship      
    regulation:      
      description: Regulation under which the container is operating      
      type: string      
      x-ngsi:      
        model: http://schema.org/Text      
        type: Property      
    responsible:      
      description: 'Responsible for the container, i.e. entity in charge of  actuating (emptying, collecting, etc)'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    serialNumber:      
      description: Serial number of the container      
      type: string      
      x-ngsi:      
        model: https://schema.org/serialNumber      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    status:      
      description: 'Container''s status from the point of view of safety. Enum:''ok , lidOpen , dropped , moved , vandalized , burning , unknown''.  -   `ok`. Container is where it must be and stands properly. `lidOpen`. Container''s lid has been opened and not closed after a certain amount of time. `dropped`. Container has been dropped for some reason. `moved`. Container has been moved from its regular position and has not come back. `vandalized`. Container has been damaged or destroyed due to vandalism. `burning`. Container is burning and an immediate action has to be taken. `unknown`. The status of the container is not known to the system'      
      enum:      
        - ok      
        - lidOpen      
        - dropped      
        - moved      
        - vandalized      
        - burning      
        - unknown      
      type: string      
      x-ngsi:      
        type: Property      
    storedWasteCode:      
      description: 'Depend on the target regulation. For Europe, check [Europe''s List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm)'      
      type: string      
      x-ngsi:      
        model: 'https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind'      
        type: Property      
    storedWasteKind:      
      description: 'Kind/s of waste stored by the container. Enum:''organic, inorganic, glass, oil, plastic, metal, paper, batteries, electronics, hazardous, other''. Or any other value which does not fit within the former. '      
      enum:      
        - organic      
        - inorganic      
        - glass      
        - oil      
        - plastic      
        - metal      
        - paper      
        - batteries      
        - electronics      
        - hazardous      
        - other      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    storedWasteOrigin:      
      description: 'Origin of the waste stored. Enum:''household, municipal, industrial, construction, hostelry, agriculture, other'' '      
      enum:      
        - household      
        - municipal      
        - industrial      
        - construction      
        - hostelry      
        - agriculture      
        - other      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    temperature:      
      description: Temperature inside the container      
      type: number      
      x-ngsi:      
        model: http://schema.org/Number      
        type: Property      
    timeInstant:      
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations'      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Datetime      
        type: Property      
    type:      
      description: 'NGSI Entity Type: It has to be WasteContainer'      
      enum:      
        - WasteContainer      
      type: string      
      x-ngsi:      
        type: Property      
    wardId:      
      description: Ward Id of the entity corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
  required:      
    - id      
    - type      
    - location      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.WasteManagement/WasteContainer/schema.json      
  x-model-tags: ""      
  x-version: 0.3.0      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### WasteContainer NGSI-v2 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 WasteContainer 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "location": {  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ],  
    "type": "Point"  
  },  
  "binCapacity": 43,  
  "binColor": "Green",  
  "binClearedTime": "2021-03-11T15:51:02+05:30",  
  "wardId": "21",  
  "binCategory": "Household Bin",  
  "license_plate": "KA23F2345",  
  "RFID": "67855734",  
  "binFillingLevel": 0.65,  
  "binFullnessThreshold": 80,  
  "binRecommendedLoad": 30,  
  "binId": "12",  
  "binMaxLoad": 75,  
  "binLoggedTime": "2021-03-01T15:51:02+05:30"  
}  
```  
</details>    
#### WasteContainer NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 WasteContainer의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ],  
      "type": "Point"  
    }  
  },  
  "binCapacity": {  
    "type": "Number",  
    "value": 43  
  },  
  "binColor": {  
    "type": "Text",  
    "value": "Green"  
  },  
  "binClearedTime": {  
    "type": "DateTime",  
    "value": "2021-03-11T15:51:02+05:30"  
  },  
  "wardId": {  
    "type": "Text",  
    "value": "21"  
  },  
  "binCategory": {  
    "type": "Text",  
    "value": "Household Bin"  
  },  
  "license_plate": {  
    "type": "Text",  
    "value": "KA23F2345"  
  },  
  "RFID": {  
    "type": "Text",  
    "value": "67855734"  
  },  
  "binFillingLevel": {  
    "type": "Number",  
    "value": 0.65  
  },  
  "binFullnessThreshold": {  
    "type": "Number",  
    "value": 80  
  },  
  "binRecommendedLoad": {  
    "type": "Number",  
    "value": 30  
  },  
  "binId": {  
    "type": "Text",  
    "value": "12"  
  },  
  "binMaxLoad": {  
    "type": "Number",  
    "value": 75  
  },  
  "binLoggedTime": {  
    "type": "DateTime",  
    "value": "2021-03-01T15:51:02+05:30"  
  }  
}  
```  
</details>    
#### 폐기물 컨테이너 NGSI-LD 키-값 예시    
다음은 키-값으로 JSON-LD 형식의 WasteContainer 예제입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "RFID": "67855734",  
  "binCapacity": 43,  
  "binCategory": "Household Bin",  
  "binClearedTime": "2021-03-11T15:51:02+05:30",  
  "binColor": "Green",  
  "binFillingLevel": 0.65,  
  "binFullnessThreshold": 80,  
  "binId": "12",  
  "binLoggedTime": "2021-03-01T15:51:02+05:30",  
  "binMaxLoad": 75,  
  "binRecommendedLoad": 30,  
  "license_plate": "KA23F2345",  
  "location": {  
    "coordinates": [  
      -8.768460000000001,  
      42.60214472222222  
    ],  
    "type": "Point"  
  },  
  "wardId": "21",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### WasteContainer NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 WasteContainer의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:wastecontainer:1021:AAWD",  
  "type": "WasteContainer",  
  "RFID": {  
    "type": "Property",  
    "value": "67855734"  
  },  
  "binCapacity": {  
    "type": "Property",  
    "value": 43  
  },  
  "binCategory": {  
    "type": "Property",  
    "value": "Household Bin"  
  },  
  "binClearedTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "binColor": {  
    "type": "Property",  
    "value": "Green"  
  },  
  "binFillingLevel": {  
    "type": "Property",  
    "value": 0.65  
  },  
  "binFullnessThreshold": {  
    "type": "Property",  
    "value": 80  
  },  
  "binId": {  
    "type": "Property",  
    "value": "12"  
  },  
  "binLoggedTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-03-11T15:51:02+05:30"  
    }  
  },  
  "binMaxLoad": {  
    "type": "Property",  
    "value": 75  
  },  
  "binRecommendedLoad": {  
    "type": "Property",  
    "value": 30  
  },  
  "license_plate": {  
    "type": "Property",  
    "value": "KA23F2345"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "coordinates": [  
        -8.768460000000001,  
        42.60214472222222  
      ],  
      "type": "Point"  
    }  
  },  
  "wardId": {  
    "type": "Property",  
    "value": "21"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
