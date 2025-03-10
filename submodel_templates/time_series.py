import aas_core3.types as aas_types
import random

try:
    import ubinascii as ubinascii
except ImportError:
    try:
        import binascii as ubinascii
    except ImportError:
        raise ImportError("Could not import 'ubinascii' from either path.")

try:
    from embedded_system.submodel_templates.submodel_template import SubmodelTemplate
except ImportError:
    try:
        from submodel_templates.submodel_template import SubmodelTemplate
    except ImportError:
        raise ImportError("Could not import 'SubmodelTemplate' from either path.")


class SegmentType:
    EXTERNAL_SEGMENT = "ExternalSegment"
    LINKED_SEGMENT = "LinkedSegment"
    INTERNAL_SEGMENT = "InternalSegment"


def random_string(length=8):
    # Generate random bytes
    random_bytes = random.getrandbits(length * 8).to_bytes(length, 'big')
    # Convert to hex string and take desired length
    return ubinascii.hexlify(random_bytes)[:length].decode()


class Record(aas_types.SubmodelElementCollection):
    """
    Class representing a Record within an InternalSegment using aas-core3.
    """

    def __init__(
            self,
            values: [aas_types.SubmodelElement]
    ):
        # Initialize parent SubmodelElementCollection
        super().__init__(id_short="Record_" + random_string(11))

        # Time property
        self.value = values


class Segment(aas_types.SubmodelElementCollection):
    """
    Class representing a Segment (e.g., InternalSegment, ExternalSegment, LinkedSegment)
    within a TimeSeries structure using aas-core3.
    """

    def __init__(
            self,
            segment_type: SegmentType,
            name: [aas_types.LangStringTextType] = None,
            description: [aas_types.LangStringTextType] = None,
            record_count: str = None,
            start_time: str = None,
            end_time: str = None,
            duration: str = None,
            sampling_interval: str = None,
            sampling_rate: str = None,
            state: str = None,
            last_update: str = None,
            records: [Record] = None,
    ):

        # Initialize parent SubmodelElementCollection
        super().__init__(id_short=str(segment_type))
        self.value = [
            aas_types.Property(
                category="CONSTANT",
                id_short="TEST",
                value="test",
                value_type=aas_types.DataTypeDefXSD.STRING
            ),
        ]

        # Add optional properties
        if name:
            self.value.append(
                aas_types.MultiLanguageProperty(
                    category="PARAMETER",
                    id_short="Name",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Meaningful name for labeling.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value=[name]
                )
            )

        if description:
            self.value.append(
                aas_types.MultiLanguageProperty(
                    self.value.append(
                        aas_types.MultiLanguageProperty(
                            category="PARAMETER",
                            id_short="Description",
                            description=[
                                aas_types.LangStringTextType(
                                    language="en",
                                    text="Short description of the time series segment.",
                                ),
                            ],
                            semantic_id=aas_types.Reference(
                                type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                                keys=[
                                    aas_types.Key(
                                        type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                        value="https://admin-shell.io/idta/TimeSeries/Segment/Name/1/1"
                                    )
                                ]
                            ),
                            qualifiers=[
                                aas_types.Qualifier(
                                    type="Cardinality",
                                    value_type=aas_types.DataTypeDefXSD.STRING,
                                    value="ZeroToOne"
                                ),
                            ],
                            value=[description]
                        )
                    )
                )
            )

        if record_count is not None:
            self.value.append(
                aas_types.Property(
                    category="VARIABLE",
                    id_short="Description",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="The amount of records stored in this time series.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/RecordCount/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.LONG,
                    value=record_count
                )
            )

        if start_time:
            self.value.append(
                aas_types.Property(
                    category="VARIABLE",
                    id_short="StartTime",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Start time of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/StartTime/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=start_time
                )
            )

        if end_time:
            self.value.append(
                aas_types.Property(
                    category="VARIABLE",
                    id_short="EndTime",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Start time of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/EndTime/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=end_time
                )
            )

        if duration:
            self.value.append(
                aas_types.Property(
                    category="VARIABLE",
                    id_short="Duration",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Start time of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/Duration/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=duration
                )
            )

        if sampling_interval is not None:
            self.value.append(
                aas_types.Property(
                    category="PARAMETER",
                    id_short="SamplingInterval",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Start time of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/SamplingInterval/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=sampling_interval
                )
            )

        if sampling_rate is not None:
            self.value.append(
                aas_types.Property(
                    category="PARAMETER",
                    id_short="SamplingRate",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Start time of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/SamplingRate/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=sampling_rate
                )
            )

        if state:
            self.value.append(
                aas_types.Property(
                    category="PARAMETER",
                    id_short="State",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="The current state of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/State/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=state
                )
            )

        if last_update:
            self.value.append(
                aas_types.Property(
                    category="PARAMETER",
                    id_short="LastUpdate",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Time of last update of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=last_update
                )
            )

        if last_update:
            self.value.append(
                aas_types.Property(
                    category="PARAMETER",
                    id_short="LastUpdate",
                    description=[
                        aas_types.LangStringTextType(
                            language="en",
                            text="Time of last update of the time series segment.",
                        ),
                    ],
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"
                            )
                        ]
                    ),
                    qualifiers=[
                        aas_types.Qualifier(
                            type="Cardinality",
                            value_type=aas_types.DataTypeDefXSD.STRING,
                            value="ZeroToOne"
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.STRING,
                    value=last_update
                )
            )

        # Add records as a collection
        if segment_type == SegmentType.INTERNAL_SEGMENT:
            records_collection = aas_types.SubmodelElementCollection(
                id_short="Records",
                description=[
                    aas_types.LangStringTextType(
                        language="en",
                        text="The internally stored records of the time series segment.",
                    ),
                ],
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="https://admin-shell.io/idta/TimeSeries/Segment/LastUpdate/1/1"
                        )
                    ]
                ),
                qualifiers=[
                    aas_types.Qualifier(
                        type="Cardinality",
                        value_type=aas_types.DataTypeDefXSD.STRING,
                        value="ZeroToOne"
                    ),
                ],
                value=[
                    aas_types.Property(
                        id_short="Record",
                        value_type=aas_types.DataTypeDefXSD.STRING
                    )
                ]
            )
            if records:
                records_collection.value.append(records)
            self.value.append(records_collection)


class TimeSeries(SubmodelTemplate):
    @classmethod
    def get_id_short(cls) -> str:
        return "TimeSeries"

    def __init__(self, new_id,
                 segments: [Segment] = None):
        super().__init__(new_id=new_id)

        # Directly add the required submodel elements One or more
        self.submodel_elements = [
            # region: Metadata : One : done
            aas_types.SubmodelElementCollection(
                id_short="Metadata",
                semantic_id=aas_types.Reference(
                    type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                    keys=[
                        aas_types.Key(
                            type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                            value="https://admin-shell.io/idta/TimeSeries/Metadata/1/1"
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
                value=[
                    aas_types.SubmodelElementCollection(
                        id_short="Metadata",
                    )
                ],

            ),

        ]

        # region: Segments : One: done
        if segments is not None:
            self.submodel_elements.append(
                aas_types.SubmodelElementCollection(
                    id_short="Segments",
                    semantic_id=aas_types.Reference(
                        type=aas_types.ReferenceTypes.EXTERNAL_REFERENCE,
                        keys=[
                            aas_types.Key(
                                type=aas_types.KeyTypes.GLOBAL_REFERENCE,
                                value="https://admin-shell.io/idta/TimeSeries/Segments/1/1"
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
                    value=segments,
                ),
            )
        # endregion
