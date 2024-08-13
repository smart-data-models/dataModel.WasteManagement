from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class CategoryEnum(Enum):
    fixed = 'fixed'
    ground = 'ground'
    other = 'other'
    portable = 'portable'
    underground = 'underground'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Status(Enum):
    ok = 'ok'
    lidOpen = 'lidOpen'
    dropped = 'dropped'
    moved = 'moved'
    vandalized = 'vandalized'
    burning = 'burning'
    unknown = 'unknown'


class StoredWasteKind(Enum):
    organic = 'organic'
    inorganic = 'inorganic'
    glass = 'glass'
    oil = 'oil'
    plastic = 'plastic'
    metal = 'metal'
    paper = 'paper'
    batteries = 'batteries'
    electronics = 'electronics'
    hazardous = 'hazardous'
    other = 'other'


class StoredWasteOrigin(Enum):
    household = 'household'
    municipal = 'municipal'
    industrial = 'industrial'
    construction = 'construction'
    hostelry = 'hostelry'
    agriculture = 'agriculture'
    other = 'other'


class Type6(Enum):
    WasteContainer = 'WasteContainer'


class WasteContainer(BaseModel):
    RFID: Optional[str] = Field(None, description='Gives the ID of the RFID reader')
    actuationHours: Optional[str] = Field(
        None, description='Hours suitable for performing actuations over the container'
    )
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    annotations: Optional[List[str]] = Field(
        None, description='Annotations about the item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    binCapacity: Optional[float] = Field(
        None,
        description='Total capacity in terms of the volume of waste the bin can hold',
    )
    binColor: Optional[str] = Field(
        None,
        description='Color of the bin. Could be used for indicating the type of waste. The color coding should follow the conventions applicable to the geographical area the bins are located',
    )
    binFullnessThreshold: Optional[float] = Field(
        None,
        description='The fullness threshold level of the bin defined as the level (in terms of percentage) when the bin full alert or notification will be generated',
    )
    binId: Optional[str] = Field(None, description='Id of the waste carrying bin')
    binLoggedTime: Optional[AwareDatetime] = Field(
        None, description="Time when the bin's level was last logged"
    )
    binMaxLoad: Optional[float] = Field(
        None, description='Maximum load (weight) that the waste bin can hold'
    )
    binRecommendedLoad: Optional[float] = Field(
        None,
        description='Recommended load (weight) that the waste bin corresponding to this observation can hold',
    )
    cargoWeight: Optional[confloat(ge=0.0)] = Field(
        None, description='Weight of the container load'
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Container's category. Enum:' fixed, ground, other, portable, underground'",
        min_length=1,
    )
    color: Optional[str] = Field(None, description='The color of the product')
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateLastCleaning: Optional[AwareDatetime] = Field(
        None, description='When the container was cleaned last time. '
    )
    dateLastEmptying: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp which represents when the container was emptied last time',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateServiceStarted: Optional[AwareDatetime] = Field(
        None, description='Date at which the container started giving service'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    fillingLevel: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None, description='Filling level of the container'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    isleId: Optional[str] = Field(
        None,
        description='Identifier (or name) of the isle where the container is placed. This attribute should be used when entities of type `WasteContainerIsle` are not being modelled specifically. Otherwise, `refWasteContainerIsle` should be used',
    )
    license_plate: Optional[str] = Field(
        None,
        description="Gives the License Plate number of the vehicle. SameAs: 'license_plate' field from GTFS Realtime message-VehicleDescriptor (https://developers.google.com/transit/gtfs-realtime/reference#message-vehicledescriptor)",
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    methaneConcentration: Optional[confloat(ge=0.0)] = Field(
        None, description='Methane (CH4) concentration inside the container'
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nextActuationDeadline: Optional[AwareDatetime] = Field(
        None,
        description='Deadline for next actuation to be performed (emptying, picking up, etc.)',
    )
    nextCleaningDeadline: Optional[AwareDatetime] = Field(
        None, description='Deadline for next cleaning'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refDevice: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None, description='Reference to the device(s) used to monitor this container'
    )
    refWasteContainerIsle: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Isle where the container is placed')
    refWasteContainerModel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description="Container's model")
    regulation: Optional[str] = Field(
        None, description='Regulation under which the container is operating'
    )
    responsible: Optional[str] = Field(
        None,
        description='Responsible for the container, i.e. entity in charge of  actuating (emptying, collecting, etc)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[str] = Field(
        None, description='Serial number of the container'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[Status] = Field(
        None,
        description="Container's status from the point of view of safety. Enum:'ok , lidOpen , dropped , moved , vandalized , burning , unknown'.  -   `ok`. Container is where it must be and stands properly. `lidOpen`. Container's lid has been opened and not closed after a certain amount of time. `dropped`. Container has been dropped for some reason. `moved`. Container has been moved from its regular position and has not come back. `vandalized`. Container has been damaged or destroyed due to vandalism. `burning`. Container is burning and an immediate action has to be taken. `unknown`. The status of the container is not known to the system",
    )
    storedWasteCode: Optional[str] = Field(
        None,
        description="Depend on the target regulation. For Europe, check [Europe's List of Waste](http://ec.europa.eu/environment/waste/framework/list.htm)",
    )
    storedWasteKind: Optional[StoredWasteKind] = Field(
        None,
        description="Kind/s of waste stored by the container. Enum:'organic, inorganic, glass, oil, plastic, metal, paper, batteries, electronics, hazardous, other'. Or any other value which does not fit within the former. ",
    )
    storedWasteOrigin: Optional[StoredWasteOrigin] = Field(
        None,
        description="Origin of the waste stored. Enum:'household, municipal, industrial, construction, hostelry, agriculture, other' ",
    )
    temperature: Optional[float] = Field(
        None, description='Temperature inside the container'
    )
    timeInstant: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the payload . There can be production environments where the attribute type is equal to the `ISO8601` string. If so, it must be considered as a synonym of `DateTime`. This attribute is kept for backwards compatibility with old FIWARE reference implementations',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity Type: It has to be WasteContainer'
    )
    wardId: Optional[str] = Field(
        None, description='Ward Id of the entity corresponding to this observation'
    )
