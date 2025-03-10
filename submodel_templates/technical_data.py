import aas_core3.types as aas_types
import aas_core3.jsonization as aas_jsonization

try:
    from embedded_system.submodel_templates.submodel_template import SubmodelTemplate
except ImportError:
    try:
        from submodel_templates.submodel_template import SubmodelTemplate
    except ImportError:
        raise ImportError("Could not import 'SubmodelTemplate' from either path.")


class TechnicalData(SubmodelTemplate):

    @classmethod
    def get_id_short(cls) -> str:
        return "TechnicalData"

    def __init__(self, new_id,
                 general_information: str,
                 technical_properties: [aas_types.SubmodelElement]):
        super().__init__(new_id=new_id)

        # region: Description

        self.description = [
            aas_types.LangStringTextType(
                language="en",
                text="Submodel containing techical data of the asset and associated product classificatons.",
            ),
            aas_types.LangStringTextType(
                language="de",
                text="Teilmodell, das die technischen Daten der Anlage und die zugehörigen Produktklassifizierungen enthält.",
            ),
        ]

        # endregion

        # region: SemanticId

        self.semantic_id = aas_types.Reference(
            type=aas_types.ReferenceTypes.MODEL_REFERENCE,
            keys=[
                aas_types.Key(
                    type=aas_types.KeyTypes.SUBMODEL,
                    value="https://admin-shell.io/ZVEI/TechnicalData/Submodel/1/2"
                )
            ]
        )

        # endregion

        # region: Elements
        self.submodel_elements = [
            # region: URIOfTheProduct : One : done
            aas_types.Property(
                id_short="GeneralInformation",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="General information, for example ordering and manufacturer information.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="General information, for example ordering and manufacturer information."
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                ],
                value_type=aas_types.DataTypeDefXSD.STRING,
                value=general_information,
            ),
            aas_types.SubmodelElementCollection(
                id_short="TechnicalProperties",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="Individual characteristics that describe the product and its technical properties.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="https://admin-shell.io/ZVEI/TechnicalData/TechnicalProperties/1/1"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="One"
                    ),
                ],
                value=technical_properties,
            ),
        ]
        #endregion

    @classmethod
    def get_html_from_submodel(cls, submodel: aas_types.Submodel):
        json = aas_jsonization.to_jsonable(submodel)

        return cls.generate_technical_html(json)

    # region: Html Generation


    @staticmethod
    def generate_technical_html(json_data):
        def format_property_name(name):
            """Format property names by replacing underscores and cleaning up special characters"""
            name = name.replace('_', ' ')
            name = name.replace('DegC', '°C')
            name = name.replace('50 60Hz', '50/60 Hz')
            return name

        def format_collection(collection):
            if not isinstance(collection, list):
                return ''

            html = '<div class="measurements-grid">'
            for item in collection:
                if item['modelType'] == 'Property':
                    formatted_name = format_property_name(item['idShort'])
                    html += f'''
                        <div class="metric">
                            <span class="metric-label">{formatted_name}</span>
                            <span class="metric-value">{item['value']}</span>
                        </div>'''
                elif item['modelType'] == 'SubmodelElementCollection':
                    html += f'''
                        <div class="nested-collection">
                            <div class="card-header">{item['idShort']}</div>
                            {format_collection(item.get('value', []))}
                        </div>'''
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
                .measurements-grid {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 1rem;
                    margin-bottom: 1rem;
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
                    padding: 1rem;
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
                }}
                .language-selector {{
                    display: flex;
                    gap: 0.5rem;
                    margin-bottom: 1rem;
                }}
                .language-button {{
                    padding: 0.5rem 1rem;
                    border: 1px solid #303f9f;
                    border-radius: 4px;
                    background: white;
                    color: #303f9f;
                    cursor: pointer;
                }}
                .language-button.active {{
                    background: #303f9f;
                    color: white;
                }}
                @media (max-width: 768px) {{
                    .measurements-grid {{
                        grid-template-columns: 1fr;
                    }}
                    .container {{
                        padding: 0.5rem;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="dashboard-title">{json_data['idShort']}</h1>
        """

        # Add language selector and descriptions
        descriptions = {desc['language']: desc['text'] for desc in json_data['description']}
        html_template += '''
            <div class="language-selector">
                <button class="language-button active" onclick="showDescription('en')">English</button>
                <button class="language-button" onclick="showDescription('de')">Deutsch</button>
            </div>
        '''

        for lang, text in descriptions.items():
            display = 'block' if lang == 'en' else 'none'
            html_template += f'<div id="desc-{lang}" class="description" style="display: {display}">{text}</div>'

        # Add JavaScript for language switching
        html_template += '''
            <script>
                function showDescription(lang) {
                    document.querySelectorAll('.description').forEach(el => el.style.display = 'none');
                    document.getElementById('desc-' + lang).style.display = 'block';
                    document.querySelectorAll('.language-button').forEach(btn => btn.classList.remove('active'));
                    event.target.classList.add('active');
                }
            </script>
        '''

        # Process submodelElements
        for element in json_data['submodelElements']:
            html_template += f'<div class="card">'
            if element['modelType'] == 'Property':
                html_template += f'''
                    <div class="card-header">{element['idShort']}</div>
                    <div class="metric">
                        <span class="metric-label">Value</span>
                        <span class="metric-value">{element['value']}</span>
                    </div>
                '''
            elif element['modelType'] == 'SubmodelElementCollection':
                html_template += f'''
                    <div class="card-header">{element['idShort']}</div>
                    {format_collection(element.get('value', []))}
                '''
            html_template += '</div>'

        html_template += """
            </div>
        </body>
        </html>
        """
        return html_template



    # endregion
