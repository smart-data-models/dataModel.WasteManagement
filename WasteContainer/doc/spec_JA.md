<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティWasteContainer  
====================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.WasteManagement/blob/master/WasteContainer/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**ゴミ箱**。  
バージョン: 0.3.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `RFID[string]`: RFIDリーダーのIDを付与する。  . Model: [https://schema.org/Text](https://schema.org/Text)- `actuationHours[string]`: 容器の上でアクチュエーションを行うのに適した時間。  . Model: [openingHours](openingHours)- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: この項目の別称  - `annotations[array]`: アイテムに関するアノテーション  . Model: [https://schema.org/Text](https://schema.org/Text)- `areaServed[string]`: サービスまたは提供品が提供される地理的な地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `binCapacity[number]`: ゴミ箱に入れることができるゴミの量を表す総容量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `binColor[string]`: ビンの色。廃棄物の種類を示すために使用され得る。色分けは、ごみ箱が設置されている地理的地域に適用される慣例に従うべきである。  . Model: [https://schema.org/Text](https://schema.org/Text)- `binFullnessThreshold[number]`: ビンが満杯のアラートまたは通知が生成されるレベル（パーセンテージで）として定義されるビンの満杯しきい値レベルです。  . Model: [https://schema.org/Number](https://schema.org/Number)- `binId[string]`: ゴミ箱の中身  . Model: [https://schema.org/Text](https://schema.org/Text)- `binLoggedTime[string]`: ビンのレベルが最後にログに記録された時間。  . Model: [https://schema.org/Text](https://schema.org/Text)- `binMaxLoad[number]`: ゴミ箱に載せることができる最大荷重（重量）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `binRecommendedLoad[number]`: この観測に対応する廃棄物容器が保持できる推奨荷重（重量）。  . Model: [https://schema.org/Number](https://schema.org/Number)- `cargoWeight[number]`: コンテナの積み荷の重量。  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: Enum:' 固定、地上、その他、携帯、地下'。  . Model: [https://schema.org/Text Containers category](https://schema.org/Text Containers category)- `color[string]`: 製品の色  . Model: [https://schema.org/color](https://schema.org/color)- `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateLastCleaning[string]`: 前回、容器を洗浄したとき。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastEmptying[string]`: コンテナが前回空になった時刻を示すタイムスタンプ。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateServiceStarted[string]`: コンテナがサービスを開始した日付。  . Model: [https://schema.org/Date](https://schema.org/Date)- `description[string]`: このアイテムの説明  - `fillingLevel[number]`: 容器の充填レベル  . Model: [https://schema.org/Number](https://schema.org/Number)- `id[*]`: エンティティの一意な識別子  - `image[string]`: アイテムの画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `isleId[string]`: コンテナが置かれるアイルの識別子（または名前）。この属性は `WasteContainerIsle` 型のエンティティを具体的にモデル化していない場合に使用する必要があります。そうでない場合は、 `refWasteContainerIsle` を使用する必要があります。  - `license_plate[string]`: 車両のナンバーを付与する。と同じです。GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)の 'license_plate' フィールド。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson リファレンス。Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygonのいずれかを指定することができる。  - `methaneConcentration[number]`: 容器内のメタン（CH4）濃度。  . Model: [https://schema.org/Number](https://schema.org/Number)- `name[string]`: このアイテムの名称です。  - `nextActuationDeadline[string]`: 次に実行される動作の期限（エンプティ、ピックアップなど）。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `nextCleaningDeadline[string]`: 次回のクリーニングの締切日  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `refDevice[array]`: このコンテナを監視するために使用されるデバイス（複数可）への参照  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerIsle[*]`: 容器が置かれるアイル  . Model: [http://schema.org/URL](http://schema.org/URL)- `refWasteContainerModel[*]`: コンテナのモデル  . Model: [http://schema.org/URL](http://schema.org/URL)- `regulation[string]`: コンテナが運用されている規制  . Model: [http://schema.org/Text](http://schema.org/Text)- `responsible[string]`: 容器の責任者、すなわち作動（空、回収など）を担当する主体  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `serialNumber[string]`: 容器のシリアル番号。  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `status[string]`: 安全性の観点から見た容器の状態。Enum:'ok , lidOpen , drop , move , vandalized , burning , unknown'.  - OK`。容器はあるべき場所にあり、きちんと立っています。lidOpen`.コンテナの蓋が開けられ、一定時間経過しても閉まらない状態です。`dropped`.コンテナが何らかの理由で落とされた。moved`.容器が定位置から移動され、戻ってきません。荒らされた`.コンテナは破壊行為によって損傷または破壊されました。燃えている`.コンテナが燃えています。すぐに対処する必要があります。不明`.コンテナの状態は、システムにはわからない。  - `storedWasteCode[string]`: 対象規制により異なる。欧州の場合、[欧州の廃棄物リスト](http://ec.europa.eu/environment/waste/framework/list.htm)を確認する。  . Model: [https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind](https://schema.org/Text As per the regulation, waste codes which precisely identifies waste origin and kind)- `storedWasteKind[string]`: コンテナで保管されている廃棄物の種類。Enum:'organic, inorganic, glass, oil, plastic, metal, paper, batteries, electronics, hazardous, other' （有機物、無機物、ガラス、油、プラスチック、金属、紙、電池、電子機器、危険物、その他）。または、前者に当てはまらないその他の値。  . Model: [https://schema.org/Text](https://schema.org/Text)- `storedWasteOrigin[string]`: 保管されている廃棄物の起源。Enum:'household, municipal, industrial, construction, hostelry, agriculture, other'.  . Model: [https://schema.org/Text](https://schema.org/Text)- `temperature[number]`: 容器内温度  . Model: [http://schema.org/Number](http://schema.org/Number)- `timeInstant[string]`: ペイロードのタイムスタンプ。実運用環境では、属性の型が `ISO8601` 文字列と等しい場合もあり得る。その場合、`DateTime` のシノニムと考える必要がある。この属性は、古いFIWAREリファレンスの実装との後方互換性のために残されている。  . Model: [https://schema.org/Datetime](https://schema.org/Datetime)- `type[string]`: NGSI エンティティタイプ。WasteContainerでなければならない  - `wardId[string]`: 区 この観測に対応するエンティティの ID。  . Model: [https://schema.org/Text](https://schema.org/Text)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `location`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
WasteContainer:    
  description: 'A waste container'    
  properties:    
    RFID:    
      description: 'Gives the ID of the RFID reader.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    actuationHours:    
      description: 'Hours suitable for performing actuations over the container.'    
      type: string    
      x-ngsi:    
        model: openingHours    
        type: Property    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binCapacity:    
      description: 'Total capacity in terms of the volume of waste the bin can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    binColor:    
      description: 'Color of the bin. Could be used for indicating the type of waste. The color coding should follow the conventions applicable to the geographical area the bins are located.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binFullnessThreshold:    
      description: 'The fullness threshold level of the bin defined as the level (in terms of percentage) when the bin full alert or notification will be generated.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    binId:    
      description: 'Id of the waste carrying bin'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binLoggedTime:    
      description: 'Time when the bin''s level was last logged.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    binMaxLoad:    
      description: 'Maximum load (weight) that the waste bin can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    binRecommendedLoad:    
      description: 'Recommended load (weight) that the waste bin corresponding to this observation can hold.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cargoWeight:    
      description: 'Weight of the container load.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    category:    
      description: 'Enum:'' fixed, ground, other, portable, underground'''    
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
        model: 'https://schema.org/Text Containers category'    
        type: Property    
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
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
      description: 'Timestamp which represents when the container was emptied last time.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateServiceStarted:    
      description: 'Date at which the container started giving service.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Date    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fillingLevel:    
      description: 'Filling level of the container'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    id:    
      anyOf: &wastecontainer_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    isleId:    
      description: 'Identifier (or name) of the isle where the container is placed. This attribute should be used when entities of type `WasteContainerIsle` are not being modelled specifically. Otherwise, `refWasteContainerIsle` should be used.'    
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: GeoProperty    
    methaneConcentration:    
      description: 'Methane (CH4) concentration inside the container.'    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nextActuationDeadline:    
      description: 'Deadline for next actuation to be performed (emptying, picking up, etc.).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    nextCleaningDeadline:    
      description: 'Deadline for next cleaning.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      description: 'Reference to the device(s) used to monitor this container'    
      items:    
        anyOf: *wastecontainer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      minItems: 1    
      type: array    
      uniqueItems: true    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    refWasteContainerIsle:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Isle where the container is placed'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    refWasteContainerModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Container''s model'    
      x-ngsi:    
        model: http://schema.org/URL    
        type: Relationship    
    regulation:    
      description: 'Regulation under which the container is operating'    
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
      description: 'list of uri pointing to additional resources about the item'    
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
      description: 'Serial number of the container.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Container''s status from the point of view of safety. Enum:''ok , lidOpen , dropped , moved , vandalized , burning , unknown''.  -   `ok`. Container is where it must be and stands properly. `lidOpen`. Container''s lid has been opened and not closed after a certain amount of time. `dropped`. Container has been dropped for some reason. `moved`. Container has been moved from its regular position and has not come back. `vandalized`. Container has been damaged or destroyed due to vandalism. `burning`. Container is burning and an immediate action has to be taken. `unknown`. The status of the container is not known to the system.'    
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
      description: 'Depend on the target regulation. For Europe, check [Europe''s List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm).'    
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
      description: 'Temperature inside the container'    
      type: number    
      x-ngsi:    
        model: http://schema.org/Number    
        type: Property    
    timeInstant:    
      description: 'Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations.'    
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
      description: 'Ward Id of the entity corresponding to this observation.'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### WasteContainer NGSI-v2 key-value の例。  
以下はWasteContainerをJSON-LD形式でkey-valuesにした例です。これは、`options=keyValues`を使用した場合にNGSI-v2と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### WasteContainer NGSI-v2 正規化例  
以下は、WasteContainerをJSON-LD形式で正規化した例である。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "type": "number",  
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
    "type": "number",  
    "value": 0.65  
  },  
  "binFullnessThreshold": {  
    "type": "number",  
    "value": 80  
  },  
  "binRecommendedLoad": {  
    "type": "number",  
    "value": 30  
  },  
  "binId": {  
    "type": "Text",  
    "value": "12"  
  },  
  "binMaxLoad": {  
    "type": "number",  
    "value": 75  
  },  
  "binLoggedTime": {  
    "type": "DateTime",  
    "value": "2021-03-01T15:51:02+05:30"  
  }  
}  
```  
</details>  
#### WasteContainer NGSI-LD キー値例  
WasteContainerをJSON-LD形式でkey-valuesにした例です。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
        "iudx:WmgmtBin",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### WasteContainer NGSI-LD 正規化例  
以下は、WasteContainerをJSON-LD形式で正規化した例である。これはオプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
        "type": "Text",  
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
        "iudx:WmgmtBin",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.WasteManagement/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
