from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, confloat, constr


class CategoryEnum(Enum):
    dumpster = 'dumpster'
    trashCan = 'trashCan'
    wheelieBin = 'wheelieBin'
    other = 'other'


class Feature(Enum):
    wheels = 'wheels'
    lid = 'lid'
    roundedLid = 'roundedLid'
    insertHoles = 'insertHoles'
    lockable = 'lockable'
    other = 'other'


class MadeOf(Enum):
    plastic = 'plastic'
    wood = 'wood'
    metal = 'metal'
    other = 'other'


class Type(Enum):
    WasteContainerModel = 'WasteContainerModel'


class WasteContainerModel(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    annotations: Optional[List[str]] = Field(
        None, description='Annotations about the item'
    )
    brandName: Optional[str] = Field(None, description='Name of the brand')
    cargoVolume: Optional[confloat(ge=0.0)] = Field(
        None, description='Total volume the container can hold'
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Container’s category. Enum:'dumpster, trashCan, wheelieBin, other'.  dumpster . See [https://en.wikipedia.org/wiki/Dumpster](https://en.wikipedia.org/wiki/Dumpster)",
        min_length=1,
    )
    color: Optional[str] = Field(None, description='The color of the product')
    compliantWith: Optional[List[str]] = Field(
        None,
        description='A list of standards to which the container is compliant  with (ex. UNE-EN 840-2:2013). ',
        min_length=0,
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    depth: Optional[confloat(ge=0.0)] = Field(
        None, description='Depth of the container'
    )
    description: Optional[str] = Field(None, description='A description of this item')
    features: Optional[List[Feature]] = Field(
        None,
        description="A list of container features. Enum:'wheels, lid, roundedLid, insertHoles, lockable'. Any other value meaningful for the application",
        min_length=1,
    )
    height: Optional[confloat(ge=0.0)] = Field(
        None, description='Height of the container'
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
    insertHolesNumber: Optional[confloat(ge=0.0)] = Field(
        None, description='Number of insert holes the container has'
    )
    madeOf: Optional[MadeOf] = Field(
        None,
        description="Material the container is made of. Enum:' plastic , wood, metal, other '",
    )
    madeOfCode: Optional[str] = Field(
        None, description='Material Code as per standard tables. '
    )
    manufacturerName: Optional[str] = Field(
        None, description='Name of the manufacturer. '
    )
    maximumLoad: Optional[confloat(ge=0.0)] = Field(
        None, description="Maximum load the container can hold safely. Unit:'Kilogram'"
    )
    modelName: Optional[str] = Field(
        None,
        description='Name of the model as given by the manufacturer. This attribute is different than name which is just a codename usually given by municipalities',
    )
    name: Optional[str] = Field(None, description='The name of this item')
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
    recommendedLoad: Optional[confloat(ge=0.0)] = Field(
        None,
        description="Manufacturer recommended load for the container. Unit:'Kilogram'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity Type: It has to be WasteContainerModel'
    )
    weight: Optional[confloat(ge=0.0)] = Field(
        None, description='Weight of the container'
    )
    width: Optional[confloat(ge=0.0)] = Field(
        None, description='Width of the container'
    )
