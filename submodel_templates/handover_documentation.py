import aas_core3.types as aas_types
from aas_core3.types import SubmodelElementCollection, Property
import aas_core3.jsonization as aas_jsonization

try:
    from embedded_system.submodel_templates.submodel_template import SubmodelTemplate
except ImportError:
    try:
        from submodel_templates.submodel_template import SubmodelTemplate
    except ImportError:
        raise ImportError("Could not import 'SubmodelTemplate' from either path.")


class HandoverDocumentationEntity(aas_types.ReferenceElement):
    def __init__(self, document_reference: aas_types.Reference):
        super().__init__()

        self.id_short = "DocumentEntity"
        self.category = "PARAMETER"
        self.description = [
            aas_types.LangStringTextType(
                language="en",
                text="States, that the described Entity is an important entity for documentation of the superordinate Asset of the Asset Administration Shell. Note: typically, such Entities are well-identified sub-parts of the Asset, such as supplier parts delivered to the manufacturer of the Asset.",
            ),
        ]
        self.semantic_id = aas_types.Reference(
            type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
            keys=[
                aas_types.Key(
                    type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                    value="https://admin-shell.io/vdi/2770/1/0/EntityForDocumentation"
                )
            ]
        )
        self.value = document_reference


class HandoverDocumentationId(aas_types.SubmodelElementCollection):
    def __init__(self,
                 document_domain_id: str,
                 document_identifier: str,
                 document_is_primary: bool
                 ):
        super().__init__()
        self.id_short = "DocumentId"

        self.value = [
            aas_types.Property(
                id_short="DocumentDomainId",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organisation.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABH994#003"
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
                value=document_domain_id,
                value_type=aas_types.DataTypeDefXSD.STRING,
            ),
            aas_types.Property(
                id_short="DocumentIdentifier",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Identification number of the Document within a given domain, e.g. the providing organisation.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAO099#004"
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
                value=document_identifier,
                value_type=aas_types.DataTypeDefXSD.STRING,
            ),
            aas_types.Property(
                id_short="DocumentIsPrimary",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organisation.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABH994#003"
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
                value='true' if document_is_primary else 'false',
                value_type=aas_types.DataTypeDefXSD.BOOLEAN,
            ),
        ]


class HandoverDocumentationClassification(aas_types.SubmodelElementCollection):
    def __init__(self,
                 class_id: str,
                 class_name: [aas_types.LangStringTextType],
                 classification_system: str
                 ):
        super().__init__()
        self.id_short = "DocumentClassification"

        self.value = [
            aas_types.Property(
                id_short="ClassId",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organisation.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABH994#003"
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
                value=class_id,
                value_type=aas_types.DataTypeDefXSD.STRING,
            ),
            aas_types.MultiLanguageProperty(
                id_short="ClassName",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Identification number of the Document within a given domain, e.g. the providing organisation.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAO099#004"
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
                value=class_name
            ),
            aas_types.Property(
                id_short="ClassificationSystem",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Identification of the domain in which the given DocumentId is unique. The domain ID can e.g., be the name or acronym of the providing organisation.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABH994#003"
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
                value=classification_system,
                value_type=aas_types.DataTypeDefXSD.STRING,
            ),
        ]


class HandoverDocumentationVersion(aas_types.SubmodelElementCollection):
    def __init__(self,
                 language: str,
                 version: str,
                 title: [aas_types.LangStringTextType],
                 subtitle: [aas_types.LangStringTextType] = None,
                 description: [aas_types.LangStringTextType] = None,
                 keywords: [aas_types.LangStringTextType] = None,
                 status_set_date: str = None,
                 status_value: str = None, organization_short_name: str = None,
                 organization_official_name: str = None, digital_file: str = None,
                 preview_file: str = None):
        super().__init__()
        self.id_short = "DocumentVersion"
        self.value = [
            # Language property
            aas_types.Property(
                id_short="Language__00__",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="This property contains a list of languages used within the DocumentVersion. Each property codes one language identification according to ISO 639-1 or ISO 639-2 used in the Document."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAN468#009"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="OneToMany",
                        semantic_id=aas_types.Reference(
                            type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                            keys=[
                                aas_types.Key(
                                    type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                    value="https://admin-shell.io/SubmodelTemplates/Cardinality/1/0"
                                )
                            ]
                        )
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="en",
                        semantic_id=aas_types.Reference(
                            type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                            keys=[
                                aas_types.Key(
                                    type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                    value="https://admin-shell.io/SubmodelTemplates/ExampleValue/1/0"
                                )
                            ]
                        )
                    )
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=language
            ),
            # Version property
            aas_types.Property(
                id_short="Version",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Design that partly deviates from the previous"
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAP003#005"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="V1.2"
                    )
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=version
            ),
            # Title property
            aas_types.MultiLanguageProperty(
                id_short="Title",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Denotes the focus of the document and has a referential or communicative function, which is to refer to the content, subject matter or theme of the document"
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABG940#004"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Examplary title@en"
                    )
                ],
                value=title
            )
        ]

        if subtitle is not None:
            self.value.append(aas_types.MultiLanguageProperty(
                id_short="SubTitle",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="List of language-dependent subtitles of the Document."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABH998#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="ZeroToOne"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Examplary subtitle@en"
                    )
                ],
                value=subtitle
            ))

        if description is not None:
            self.value.append(aas_types.MultiLanguageProperty(
                id_short="Description",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Text note"
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-AAN466#004"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Abstract@en"
                    )
                ],
                value=description
            ))

        if keywords is not None:
            self.value.append(aas_types.MultiLanguageProperty(
                id_short="KeyWords",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="List of language-dependent keywords of the Document."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABH999#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Examplary keywords@en"
                    )
                ],
                value=keywords
            ))

        if status_set_date is not None:
            self.value.append(aas_types.Property(
                id_short="StatusSetDate",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Date when the document status was set. Format is YYYY-MM-dd."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABI000#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="2020-02-06"
                    )
                ],
                value_type=aas_types.DataTypeDefXSD.DATE,
                value=status_set_date
            ))

        if status_value is not None:
            self.value.append(aas_types.Property(
                id_short="StatusValue",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Each document version represents a point in time in the document life cycle."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABI001#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Released"
                    )
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=status_value
            ))

        if organization_short_name is not None:
            self.value.append(aas_types.Property(
                id_short="OrganizationShortName",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Organization short name of the author of the Document."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABI002#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Example company"
                    )
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=organization_short_name
            ))

        if organization_official_name is not None:
            self.value.append(aas_types.Property(
                id_short="OrganizationOfficialName",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Official name of the organization of the author of the Document."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABI004#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="Example company Ltd."
                    )
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=organization_official_name
            ))

        if digital_file is not None:
            self.value.append(aas_types.File(
                id_short="DigitalFile__00__",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Note: each DigitalFile represents the same content or Document version, but can be provided in different technical formats (PDF, PDFA, html, etc.) or by a link."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABK126#003"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="OneToMany"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="docu_cecc_fullmanual_DE.PDF"
                    )
                ],
                content_type="application/pdf",
                value=digital_file
            ))

        if preview_file is not None:
            self.value.append(aas_types.File(
                id_short="PreviewFile__00__",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Provides a preview image of the DocumentVersion, e.g. first page, in a commonly used image format and low resolution."
                    )
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="0173-1#02-ABK127#002"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="ZeroToOne"
                    ),
                    aas_types.Qualifier(
                        type="ExampleValue",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="docu_cecc_fullmanual_DE.jpg"
                    )
                ],
                content_type="image/jpeg",
                value=preview_file
            ))
        # Remove None entries from the list


class HandoverDocumentationDocument(aas_types.SubmodelElementCollection):
    def __init__(self, document_id: HandoverDocumentationId, classification: HandoverDocumentationClassification,
                 document_version: HandoverDocumentationVersion, document_entity: HandoverDocumentationEntity):
        super().__init__()
        self.id_short = "HandoverDocumentation__"
        self.value = [
            document_id,
            classification,
            document_version,
            document_entity
        ]


class DocumentVersionVisitor(aas_types.PassThroughVisitor):

    def __init__(self, document_id):
        super().__init__()
        self.return_rows = f"""
                        """

    def visit_property(self, that: Property):
        new_row = f"""<tr>
                        <td>{that.id_short}</td>
                        <td class="value">{that.value}</td>
                    </tr>"""
        self.return_rows += new_row

    def get_results(self):
        return self.return_rows + """
                        """


class DocumentVisitor(aas_types.PassThroughVisitor):

    def __init__(self, document_name):
        super().__init__()
        self.return_html_table = f"""
        <details>
                                <summary>Click to view: {document_name}</summary>
 
                            

            <table>
            <thead>
                <tr>
                    <th>Property</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
            """

    def visit_submodel_element_collection(
            self, that: SubmodelElementCollection
    ):
        for element in that.value:
            document_visitor = DocumentVersionVisitor(":" + element.id_short)
            document_visitor.visit(element)
            self.return_html_table += document_visitor.get_results()

    def get_results(self):
        return self.return_html_table + """
            </tbody>
        </table>
        </details>
        """


class Visitor(aas_types.PassThroughVisitor):
    end_html = """
        <details>
        <summary>Click to view: Document</summary>"""

    def visit_submodel_element_collection(
            self, that: SubmodelElementCollection
    ):
        if that.id_short.startswith("Document__"):
            for element in that.value:
                document_visitor = DocumentVisitor(element.id_short)
                document_visitor.visit(element)
                self.end_html += document_visitor.get_results()

    def get_results(self):
        return self.end_html + "</details>"


class HandoverDocumentation(SubmodelTemplate):

    @classmethod
    def get_id_short(cls) -> str:
        return "HandoverDocumentation"

    def __init__(self, new_id,
                 documents: [HandoverDocumentationDocument]):
        super().__init__(new_id=new_id)

        self.description = [
            aas_types.LangStringTextType(
                language="en",
                text="The Submodel defines a set meta data for the handover of documentation from the manufacturer to the operator for industrial equipment.",
            ),
        ]
        self.semantic_id = aas_types.Reference(
            type=aas_types.ReferenceTypes.MODEL_REFERENCE,
            keys=[
                aas_types.Key(
                    type=aas_types.KeyTypes.SUBMODEL,
                    value="0173-1#01-AHF578#003"
                )
            ]
        )

        self.submodel_elements = documents
        document_nr = 0
        for submodel_element in self.submodel_elements:

            if document_nr < 10:
                document_nr_two_digit = '0' + str(document_nr)
            else:
                document_nr_two_digit = document_nr
            submodel_element.id_short = f"Document__{document_nr_two_digit}__"
            document_nr += 1

    @classmethod
    def get_html_from_submodel(cls, submodel: aas_types.Submodel):
        json = aas_jsonization.to_jsonable(submodel)
        return cls.generate_documentation_html(json)

    @staticmethod
    def generate_documentation_html(json_data):
        def format_property(prop):
            """Format a single property into HTML"""
            if prop['modelType'] == 'Property':
                return f'''
                    <div class="metric">
                        <span class="metric-label">{prop['idShort']}</span>
                        <span class="metric-value">{prop['value']}</span>
                    </div>'''
            elif prop['modelType'] == 'MultiLanguageProperty':
                value = prop['value'][0]['text'] if prop['value'] else ''
                return f'''
                    <div class="metric">
                        <span class="metric-label">{prop['idShort']}</span>
                        <span class="metric-value">{value}</span>
                    </div>'''
            elif prop['modelType'] == 'File':
                return f'''
                    <div class="metric">
                        <span class="metric-label">{prop['idShort']}</span>
                        <span class="metric-value">
                            <a href="{prop['value']}" target="_blank" class="file-link">
                                View Document ({prop['contentType']})
                            </a>
                        </span>
                    </div>'''
            elif prop['modelType'] == 'ReferenceElement':
                ref_value = prop['value']['keys'][0]['value'] if prop['value']['keys'] else ''
                return f'''
                    <div class="metric">
                        <span class="metric-label">{prop['idShort']}</span>
                        <span class="metric-value">
                            <a href="{ref_value}" target="_blank" class="reference-link">
                                View Reference
                            </a>
                        </span>
                    </div>'''
            return ''

        def format_collection(collection):
            """Format a collection of properties into HTML"""
            if not isinstance(collection, list):
                return ''

            html = '<div class="measurements-grid">'
            for item in collection:
                if isinstance(item, dict):
                    if item['modelType'] == 'SubmodelElementCollection':
                        html += f'''
                            <details class="nested-collection" open>
                                <summary class="details-header">{item['idShort']}</summary>
                                <div class="details-content">
                                    {format_collection(item.get('value', []))}
                                </div>
                            </details>'''
                    else:
                        html += format_property(item)
            html += '</div>'
            return html

        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{json_data['idShort']}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f2f5;
                    color: #333;
                    line-height: 1.4;
                    display: flex;
                    justify-content: center;
                }}
                .container {{
                    width: 100%;
                    max-width: 800px;
                    margin: 1rem;
                    padding: 1rem;
                }}
                .card {{
                    background: white;
                    border-radius: 8px;
                    padding: 1.5rem;
                    margin-bottom: 1rem;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .card-header {{
                    color: #303f9f;
                    font-size: 1.1rem;
                    font-weight: 600;
                    margin-bottom: 1rem;
                    padding-bottom: 0.5rem;
                    border-bottom: 1px solid #eee;
                }}
                details {{
                    margin-bottom: 1rem;
                }}
                details > summary {{
                    list-style: none;
                    cursor: pointer;
                }}
                details > summary::-webkit-details-marker {{
                    display: none;
                }}
                .details-header {{
                    color: #303f9f;
                    font-size: 1.1rem;
                    font-weight: 600;
                    padding: 1rem;
                    background: #fff;
                    border-radius: 6px;
                    border: 1px solid #e0e0e0;
                    display: flex;
                    align-items: center;
                    transition: background-color 0.2s;
                }}
                .details-header:hover {{
                    background: #f5f5f5;
                }}
                .details-header::before {{
                    content: '▼';
                    margin-right: 0.5rem;
                    font-size: 0.8em;
                    transition: transform 0.2s;
                }}
                details:not([open]) > .details-header::before {{
                    transform: rotate(-90deg);
                }}
                .details-content {{
                    padding: 1rem;
                    margin-top: 0.5rem;
                }}
                .measurements-grid {{
                    display: grid;
                    grid-template-columns: 1fr;
                    gap: 1rem;
                }}
                .metric {{
                    background: #f8f9fa;
                    padding: 1rem;
                    border-radius: 6px;
                    font-size: 0.95rem;
                    display: flex;
                    justify-content: space-between;
                    align-items: flex-start;
                    border: 1px solid #e0e0e0;
                }}
                .metric-label {{
                    color: #444;
                    font-size: 0.9rem;
                    flex: 1;
                    padding-right: 1rem;
                }}
                .metric-value {{
                    color: #1976d2;
                    font-weight: 500;
                    text-align: right;
                    flex: 1;
                }}
                .nested-collection {{
                    grid-column: 1 / -1;
                    background: #f8f9fa;
                    padding: 0;
                    border-radius: 6px;
                    border: 1px solid #e0e0e0;
                }}
                .description {{
                    color: #666;
                    font-size: 0.95rem;
                    margin-bottom: 1.5rem;
                    font-style: italic;
                    background: #fff;
                    padding: 1rem;
                    border-radius: 6px;
                    border: 1px solid #e0e0e0;
                }}
                .dashboard-title {{
                    color: #1a237e;
                    font-size: 1.6rem;
                    font-weight: bold;
                    margin: 0 0 1rem 0;
                    text-align: left;
                }}
                .file-link, .reference-link {{
                    color: #1976d2;
                    text-decoration: none;
                    padding: 0.25rem 0.5rem;
                    border-radius: 4px;
                    background: #e3f2fd;
                    transition: background-color 0.2s;
                }}
                .file-link:hover, .reference-link:hover {{
                    background: #bbdefb;
                }}
                @media (max-width: 768px) {{
                    .container {{
                        margin: 0.5rem;
                        padding: 0.5rem;
                    }}
                    .metric {{
                        flex-direction: column;
                    }}
                    .metric-value {{
                        text-align: left;
                        margin-top: 0.5rem;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="dashboard-title">{json_data['idShort']}</h1>

                <div class="description">
                    {json_data['description'][0]['text']}
                </div>
        """

        # Process submodelElements
        for element in json_data['submodelElements']:
            if element['modelType'] == 'SubmodelElementCollection':
                html_template += f'''
                <div class="card">
                    <div class="card-header">Document Information</div>
                    {format_collection(element['value'])}
                </div>
                '''

        html_template += """
            </div>
        </body>
        </html>
        """
        return html_template