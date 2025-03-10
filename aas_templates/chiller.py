import aas_core3.types as aas_types
import aas_core3.jsonization as aas_jsonization
import sys
# region: imports
try:
    from submodel_templates.digital_nameplate import *
except ImportError:
    try:
        from embedded_system.submodel_templates.digital_nameplate import *
    except ImportError:
        raise ImportError("Could not import 'digital_nameplate' from either path.")

try:
    from submodel_templates.handover_documentation import *
except ImportError:
    try:
        from embedded_system.submodel_templates.handover_documentation import *
    except ImportError:
        raise ImportError("Could not import 'handover_documentation' from either path.")

try:
    from submodel_templates.technical_data import *
except ImportError:
    try:
        from embedded_system.submodel_templates.technical_data import *
    except ImportError:
        raise ImportError("Could not import 'technical_data' from either path.")

try:
    from submodel_templates.time_series import *
except ImportError:
    try:
        from embedded_system.submodel_templates.time_series import *
    except ImportError:
        raise ImportError("Could not import 'time_series' from either path.")


# endregion

class Chiller(aas_types.Environment):
    serial_number = "aaabbbccc"

    def __init__(self):
        self.asset_information = aas_types.AssetInformation(
            asset_kind=aas_types.AssetKind.TYPE
        )

        self.asset_information.default_thumbnail = aas_types.Resource(
            content_type="image/png",  # MIME type of the image
            path="https://example.com/assets/thumbnails/default-thumbnail.png"  # Path or URL to the thumbnail
        )

        self.id = "id:embedded_system:" + self.serial_number
        self.name = "Chiller"
        self.id_short = "Chiller"
        self.asset_information = aas_types.AssetInformation(
            asset_type="Instance",
            asset_kind=aas_types.AssetKind.INSTANCE,
        )

        # region: Concept Descriptions

        concept_db = aas_types.ConceptDescription(
            id=self.id + ":concepts:db",
            is_case_of=[
                aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.CONCEPT_DESCRIPTION,
                            value="reference to [dB]"
                        )
                    ]
                )
            ]
        )

        # endregion

        # region: Wifi template
        submodel_chiller_wifi_ap = aas_types.Submodel(
            id=self.id + ":wifi",
            id_short="WifiAccessPoint",
            description=[
                aas_types.LangStringTextType(
                    language="de",
                    text="Enthält die Wifi Access Point Konfiguration",
                ),
                aas_types.LangStringTextType(
                    language="en",
                    text="Contains the Wifi access point configuration data",
                ),
            ],
            submodel_elements=[
                # SSID property
                aas_types.Property(
                    id_short="SSID",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="AAS-M5StackCore2",
                ),
                # Password property
                aas_types.Property(
                    id_short="Password",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="12345678",
                ),
                # Operation to update SSID credentials
                aas_types.Operation(
                    id_short="UpdateSSIDCredentials",
                    input_variables=[
                        aas_types.OperationVariable(
                            value=aas_types.Property(
                                id_short="NewSSID",
                                value_type=aas_types.DataTypeDefXSD.STRING,
                                value=None,
                            )
                        ),
                        aas_types.OperationVariable(
                            value=aas_types.Property(
                                id_short="NewPassword",
                                value_type=aas_types.DataTypeDefXSD.STRING,
                                value=None,
                            )
                        ),
                    ],
                    output_variables=[
                        aas_types.OperationVariable(
                            value=aas_types.Property(
                                id_short="Result",
                                value_type=aas_types.DataTypeDefXSD.STRING,
                                value=None,
                            )
                        ),
                    ],
                ),
            ]
        )
        # endregion

        # region: Machine View
        # This is a custom submodel for feeding data to the ui
        submodel_chiller_machine_view = aas_types.Submodel(
            id="urn:zhaw:ims:embedded_system:543fsfds99342:machineview",
            id_short="MachineView",
            description=[
                aas_types.LangStringTextType(
                    language="en",
                    text="Contains the Wifi access point configuration data",
                ),
            ],
            submodel_elements=[
                # SSID property
                aas_types.Property(
                    id_short="FirstDisplay",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="AAS-M5StackCore2",
                ),
                # Password property
                aas_types.Property(
                    id_short="SecondDisplay",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="12345678",
                )
            ]
        )
        # endregion

        # region: Digital Nameplate with template
        # Definition from template
        submodel_chiller_digital_nameplate = DigitalNameplate(
            new_id="urn:zhaw:ims:embedded_system:" + self.serial_number + ":digitalnameplate",
            property_uri_of_the_product="https://www.smcworld.com/webcatalog/s3s/ja-jp/detail/?partNumber=HRS050-AF-20",
            property_manufacturer_name=[
                aas_types.LangStringTextType(
                    language="en",
                    text="SMC Corporation"
                ),
                aas_types.LangStringTextType(
                    language="de",
                    text="SMC Firma"
                ),
            ],
            property_manufacturer_product_designation=[
                aas_types.LangStringTextType(
                    language="de",
                    text="Chiller"
                )
            ],
            property_contact_information=[
                aas_types.Property(
                    id_short="RoleOfContactPerson",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="<RoleOfContactPerson>",
                ),
                aas_types.Property(
                    id_short="Street",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="Dorfstrasse 7",
                ),
                aas_types.Property(
                    id_short="Zipcode",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="8484",
                ),
                aas_types.Property(
                    id_short="CityTown",
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value="Weisslingen",
                ),
                aas_types.MultiLanguageProperty(
                    id_short="NationalCode",
                    value=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="CH"
                        )
                    ]
                ),
            ],
            property_manufacturer_product_root=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Temperature Control Equipment"
                        )
                    ],
            property_manufacturer_product_family=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Thermo-Chillers Standard Type"
                        )
                    ],
            property_manufacturer_product_type=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="HRS050"
                        )
                    ],
            property_order_code_of_manufacturer=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="HRS050-AF-20"
                        )
                    ],
            property_product_article_number_of_manufacturer=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="HRS050-AF-20"
                        )
                    ],
            property_serial_number="AP1171",
            property_year_of_construction="2022",
            property_date_of_manufacturer="2/28/2022",
            property_hardware_version=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="V1"
                        )
                    ],
            property_firmware_version=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Vx",
                        )
                    ],
            property_software_version=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Not applicable",
                        )
                    ],
            property_country_of_origin="Japan"

        )

        # endregion

        #region: Time Series
        time_series_internal_segment = Segment(
            segment_type=SegmentType.INTERNAL_SEGMENT,
        )
        submodel_chiller_time_series = TimeSeries(
            new_id=self.id + ":timeseries",
            segments=[time_series_internal_segment],
        )
        # endregion

        # region: Technical Data
        technical_properties = [
            aas_types.Property(
                id_short="CoolingMethod",
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="Air-cooled refrigeration"
            ),
            aas_types.Property(
                id_short="Refrigerant",
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="R410A (HFC)"
            ),
            aas_types.Property(
                id_short="Refrigerant charge [kg]",
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="0.65"
            ),
            aas_types.Property(
                id_short="Control method",
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="0.65"
            ),
            aas_types.Property(
                id_short="Ambient temperature/Humidity/Altitude",
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="Temperature: 5 to 40 °C, High-temperature environment specification (option): 5 to 45 °C, Humidity: 30 to 70 %, Altitude: less than 3000 m"
            ),
            aas_types.Property(
                id_short="NoiseLevelAt50_60Hz_dB",  # or "NoiseLevel_50_60Hz_dB"
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="65/68"
            ),
            aas_types.Property(
                id_short="Weight_Kg",  # or "Weight_kg"
                value_type=aas_types.DataTypeDefXSD.DECIMAL,
                value="69"
            ),
            aas_types.Property(
                id_short="PipeThreadType",
                value_type=aas_types.DataTypeDefXSD.STRING,
                value="G (with PT-G conversion fitting set)"
            ),
            aas_types.SubmodelElementCollection(
                id_short="Circulating fluid system",
                value=[
                    aas_types.Property(
                        id_short="CirculatingFluid",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Tap water, 15 % ethylene glycol aqueous solution"
                    ),
                    aas_types.Property(
                        id_short="SetTemperatureRange_DegC",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="5 to 40"
                    ),
                    aas_types.Property(
                        id_short="CoolingCapacity50_60Hz_W",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="4700/5100"
                    ),
                    aas_types.Property(
                        id_short="HeatingCapacity50_60Hz_W",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="1100/1400"
                    ),
                    aas_types.Property(
                        id_short="TemperatureStability_DegC",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="+/-0.1"
                    ),
                    aas_types.Property(
                        id_short="TankCapacity_L",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Approx. 5"
                    ),
                    aas_types.Property(
                        id_short="PortSize",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Rc1/2"
                    ),
                    aas_types.Property(
                        id_short="Fluid contact material",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Stainless steel, Copper (Heat exchanger brazing), Bronze, Alumina ceramic, Carbon, PP, PE, POM, FKM, EPDM, PVC"
                    ),
                ]
            )
        ]

        submodel_chiller_technical_data = TechnicalData(
            new_id=self.id + ":timeseries",
            general_information='general information',
            technical_properties=technical_properties
        )

        # endregion

        # region: Handover Documentation

        submodel_chiller_handover_documentation_id = HandoverDocumentationId(
            document_domain_id="Catalog-Best-Guide",
            document_identifier="cat43-chiller-feature_en",
            document_is_primary=True
        )

        submodel_chiller_handover_documentation_classification = HandoverDocumentationClassification(
            class_id="DE",
            class_name=[
                aas_types.LangStringTextType(
                    language="en",
                    text="Catalogues Advertising documents"
                ),
            ],
            classification_system="IEC 61355-1:2008"
        )

        submodel_chiller_handover_documentation_version = HandoverDocumentationVersion(
            language="en",
            version="1.0.0",
            title=[
                aas_types.LangStringTextType(
                    language="en",
                    text="cat43-chiller-feature_en"
                ),
            ],
            digital_file="https://ca01.smcworld.com/catalog/BEST-Guide-en/pdf/cat43-chiller-feature_en.pdf"
        )

        submodel_chiller_handover_documentation_entity = HandoverDocumentationEntity(
            document_reference=aas_types.Reference(
                type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                keys=[
                    aas_types.Key(
                        type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                        value="https://ca01.smcworld.com/catalog/BEST-Guide-en/pdf/cat43-chiller-feature_en.pdf"
                    )
                ]
            )
        )

        submodel_chiller_handover_documentation_document_1 = HandoverDocumentationDocument(
            document_id=submodel_chiller_handover_documentation_id,
            classification=submodel_chiller_handover_documentation_classification,
            document_version=submodel_chiller_handover_documentation_version,
            document_entity=submodel_chiller_handover_documentation_entity
        )

        submodel_chiller_handover_documentation = HandoverDocumentation(
            new_id=self.id + ":handoverdocumentation",
            documents=[
                submodel_chiller_handover_documentation_document_1
            ]
        )

        # endregion


        super().__init__(asset_administration_shells=[
            aas_types.AssetAdministrationShell(
                id=self.id + ":shell",
                asset_information=aas_types.AssetInformation(
                    asset_kind=aas_types.AssetKind.TYPE,
                    global_asset_id=self.id
                )
            )
        ],
            submodels=[
                submodel_chiller_digital_nameplate,
                submodel_chiller_time_series,
                submodel_chiller_wifi_ap,
                submodel_chiller_machine_view,
                submodel_chiller_technical_data,
                submodel_chiller_handover_documentation
            ]
        )
