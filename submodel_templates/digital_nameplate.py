import aas_core3.types as aas_types

try:
    from embedded_system.submodel_templates.submodel_template import SubmodelTemplate
except ImportError:
    try:
        from submodel_templates.submodel_template import SubmodelTemplate
    except ImportError:
        raise ImportError("Could not import 'SubmodelTemplate' from either path.")


class DigitalNameplate(SubmodelTemplate):

    @classmethod
    def get_id_short(cls) -> str:
        return "DigitalNameplate"

    def __init__(self, new_id,
                 property_uri_of_the_product,
                 property_manufacturer_name,
                 property_manufacturer_product_designation,
                 property_contact_information,
                 property_manufacturer_product_root: [aas_types.LangStringTextType] = None,
                 property_manufacturer_product_family: [aas_types.LangStringTextType] = None,
                 property_manufacturer_product_type: [aas_types.LangStringTextType] = None,
                 property_order_code_of_manufacturer: [aas_types.LangStringTextType] = None,
                 property_product_article_number_of_manufacturer: [aas_types.LangStringTextType] = None,
                 property_serial_number=None,
                 property_year_of_construction=None,
                 property_date_of_manufacturer=None,
                 property_hardware_version: [aas_types.LangStringTextType] = None,
                 property_firmware_version: [aas_types.LangStringTextType] = None,
                 property_software_version: [aas_types.LangStringTextType] = None,
                 property_country_of_origin=None,
                 property_company_logo=None):
        super().__init__(new_id=new_id)

        # Directly add the required submodel elements One or more
        self.submodel_elements = [
            # region: URIOfTheProduct : One : done
            aas_types.Property(
                id_short="URIOfTheProduct",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Note: see also [IRDI] 0112/2///61987#ABN590#001 URI of product instance",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAY811#001"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Multiplicity",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=property_uri_of_the_product,

            ),
            # endregion
            # region: ManufacturerName : One :
            aas_types.MultiLanguageProperty(
                id_short="ManufacturerName",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Note: see also [IRDI] 0112/2///61987#ABA565#007 manufacturer Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAO677#002"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Multiplicity",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                ],
                value=property_manufacturer_name
            ),
            # endregion
            # region: ManufacturerProductDesignation : One: done
            aas_types.MultiLanguageProperty(
                id_short="ManufacturerProductDesignation",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Note: see also [IRDI] 0112/2///61987#ABA567#007 name of product Note: Short designation of the product is meant. Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAW338#001"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Multiplicity",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                ],
                value=property_manufacturer_product_designation
            ),
            # endregion
            # region: ContactInformation : required: done
            aas_types.SubmodelElementCollection(
                id_short="ContactInformation",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="The SMC “ContactInformation” contains information on how to contact the manufacturer or an authorised service provider, e.g. when a maintenance service is required. Note: physical address is a mandatory property according to EU Machine Directive 2006/42/EC",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="https://admin-shell.io/zvei/nameplate/1/0/ContactInformations/ContactInformation"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Multiplicity",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                ],
                value=property_contact_information
            ),
            # endregion
        ]

        # region: ManufacturerProductRoot : ZeroToOne: done
        if property_manufacturer_product_root is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="ManufacturerProductRoot",
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAU732#001"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_manufacturer_product_root
                ),
            )
        # endregion
        # region: ManufacturerProductFamily : ZeroToOne: done
        if property_manufacturer_product_family is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="ManufacturerProductFamily",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: conditionally mandatory property according to EU Machine Directive 2006/42/EC. One of the two properties must be provided: ManufacturerProductFamily (0173-1#02-AAU731#001) or ManufacturerProductType (0173-1#02-AAO057#002).",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAU731#001"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_manufacturer_product_family
                ),
            )
        # endregion
        # region: ManufacturerProductType : ZeroToOne: done
        if property_manufacturer_product_type is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="ManufacturerProductType",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: conditionally mandatory property according to EU Machine Directive 2006/42/EC. One of the two properties must be provided: ManufacturerProductFamily (0173-1#02-AAU731#001) or ManufacturerProductType (0173-1#02-AAO057#002).",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAO057#002"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_manufacturer_product_type
                ),
            )
        # endregion
        # region: OrderCodeOfManufacturer : ZeroToOne: done
        if property_order_code_of_manufacturer is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="OrderCodeOfManufacturer",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: see also [IRDI] 0112/2///61987#ABA950#006 order code of product Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user\u2019s choice.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAO227#002"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_order_code_of_manufacturer
                ),
            )
        # endregion
        # region: ProductArticleNumberOfManufacturer : ZeroToOne: done
        if property_product_article_number_of_manufacturer is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="ProductArticleNumberOfManufacturer",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: see also [IRDI] 0112/2///61987#ABA581#006 article number Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAO676#003"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_product_article_number_of_manufacturer
                ),
            )
        # endregion
        # region: SerialNumber : ZeroToOne: done
        if property_serial_number is not None:
            self.submodel_elements.append(
                aas_types.Property(
                    id_short="SerialNumber",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: see also [IRDI] 0112/2///61987#ABA951#007 serial number.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAM556#002"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=property_serial_number
                ),
            )
        # endregion
        # region: YearOfConstruction : ZeroToOne: done
        if property_year_of_construction is not None:
            self.submodel_elements.append(
                aas_types.Property(
                    id_short="YearOfConstruction",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAP906#001"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=property_year_of_construction
                ),
            )
        # endregion
        # region: DateOfManufacture : ZeroToOne: done
        if property_date_of_manufacturer is not None:
            self.submodel_elements.append(
                aas_types.Property(
                    id_short="YearOfConstruction",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAP906#001"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.DATE,
                    value=property_date_of_manufacturer
                ),
            )
        # endregion
        # region: HardwareVersion : ZeroToOne: done
        if property_hardware_version is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="HardwareVersion",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAN270#002"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_hardware_version
                ),
            )
        # endregion
        # region: FirmwareVersion : ZeroToOne: done
        if property_firmware_version is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="FirmwareVersion",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: see also [IRDI] 0112/2///61987#ABA302#004 firmware version Note: Recommendation: property declaration as MLP is required by its semantic definition. As the property value is language independent, users are recommended to provide maximal 1 string in any language of the user’s choice.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAM985#002"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_firmware_version
                ),
            )
        # endregion
        # region: SoftwareVersion : ZeroToOne: done
        if property_software_version is not None:
            self.submodel_elements.append(
                aas_types.MultiLanguageProperty(
                    id_short="SoftwareVersion",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAM737#002"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=property_software_version
                ),
            )
        # endregion
        # region: CountryOfOrigin : ZeroToOne: done
        if property_country_of_origin is not None:
            self.submodel_elements.append(
                aas_types.Property(
                    id_short="CountryOfOrigin",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="0173-1#02-AAO259#004"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=property_country_of_origin
                ),
            )
        # endregion
        # region: SoftwareVersion : ZeroToOne: done
        if property_company_logo is not None:
            self.submodel_elements.append(
                aas_types.File(
                    id_short="CompanyLogo",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Note: mandatory property according to EU Machine Directive 2006/42/EC.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/zvei/nameplate/2/0/Nameplate/CompanyLogo"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Multiplicity",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    content_type="EMPTY",
                    value=property_company_logo
                ),
            )
        # endregion
