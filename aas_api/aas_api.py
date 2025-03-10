import aas_core3.types as aas_types
import aas_core3.jsonization as aas_jsonization

import time
import re

# region: Imports

try:
    from embedded_system.aas_api.lfu_cache import LFUCache
except ImportError:
    try:
        from aas_api.lfu_cache import LFUCache
    except ImportError:
        raise ImportError("Could not import 'LFUCache' from either path.")

try:
    import aas_util.value_only
except ImportError:
    try:
        import embedded_system.aas_util.value_only
    except ImportError:
        raise ImportError("Could not import 'aas_util' from either path.")

try:
    import ujson as ujson
except ImportError:
    try:
        import json as ujson
    except ImportError:
        raise ImportError("Could not import 'json or ujson' from either path.")

try:
    import ubinascii as ubinascii
except ImportError:
    try:
        import binascii as ubinascii
    except ImportError:
        raise ImportError("Could not import 'ubinascii' from either path.")


# endregion

def get_path_part(input_string):
    """Gets a string like 'test[0]' and returns ('test', 0)."""
    match = re.search(r'(.*)\[(\d+)\]$', input_string)  # Match the main string and the number in brackets
    if match:
        return match.group(1), int(match.group(2))  # Return the string part and the number
    return input_string, None


def get_number_from_brackets(self, input_string):
    """Return the number inside square brackets if it exists, otherwise return None."""
    match = re.search(r'\[(\d+)\]$', input_string)  # Match [number] at the end of the string
    if match:
        return int(match.group(1))  # Return the number as an integer
    return None  # No number found


class MESSAGES:
    # region: GENERAL MESSAGES

    NOT_IMPLEMENTED = "Not implemented"

    # endregion

    # region: ASSET ADMINISTRATION SHELL (AAS)

    # Errors
    ERROR_JSON_SERIALIZATION = "Error serializing AAS environment."

    # Usage
    USAGE_AAS_ENVIRONMENT = "Usage: /aas"

    # Success
    SUCCESS_GET_AAS_ENVIRONMENT = "Successfully retrieved AAS environment."
    SUCCESS_CREATE_AAS_ENVIRONMENT = "Successfully created AAS environment."

    # endregion

    # region: ASSET INFORMATION

    SUCCESS_GET_ASSET_INFORMATION = "Successfully retrieved AAS asset information."

    # endregion

    # region: SUBMODEL-REFS

    SUCCESS_GET_SUBMODEL_REFS = "Successfully retrieved AAS submodel references."

    # endregion

    # region: SUBMODEL

    # Errors
    ERROR_SUBMODEL_NOT_FOUND = "Submodel not found in AAS environment."

    # Usage
    USAGE_GET_SUBMODEL = "Usage: /aas/submodels/<submodel_identifier>"
    USAGE_PUT_SUBMODEL = "Usage: /aas/submodels/<submodel_identifier>/put"
    # Success
    SUCCESS_GET_SUBMODEL = "Successfully retrieved submodel from AAS environment."
    SUCCESS_CREATE_SUBMODEL = "Successfully created submodel in AAS environment."
    SUCCESS_UPDATE_SUBMODEL = "Successfully updated submodel in AAS environment."
    SUCCESS_DELETE_SUBMODEL = "Successfully deleted submodel from AAS environment."

    # endregion

    # region: SUBMODEL ELEMENTS

    # Errors
    ERROR_SUBMODEL_ELEMENT_NOT_FOUND = "Submodel element not found in AAS environment."

    # Usage
    USAGE_SUBMODEL_ELEMENT = "Usage: /aas/submodels/<submodel_identifier>/submodel-elements/<idShortPath>"

    # Success
    SUCCESS_GET_SUBMODEL_ELEMENT = "Successfully retrieved submodel element from AAS environment."
    SUCCESS_CREATE_SUBMODEL_ELEMENT = "Successfully created submodel element in AAS environment."
    SUCCESS_UPDATE_SUBMODEL_ELEMENT = "Successfully updated submodel element in AAS environment."
    SUCCESS_DELETE_SUBMODEL_ELEMENT = "Successfully deleted submodel element from AAS environment."

    # endregion


class AasApi:
    # region: cache
    id_short_path_cache = LFUCache(10)

    # endregion
    def __init__(self, aas: aas_types.Environment, debug=False, cache=True):
        self.aas = aas
        self.debug = debug
        self.cache = cache

    # region: search methods
    def does_submodel_exist(self, id_short):
        for submodel in self.aas.submodels:
            if submodel.id_short == id_short:
                return True
        return False

    def get_submodel_by_identifier(self, identifier):
        for submodel in self.aas.submodels:
            if submodel.id_short == identifier or self.base64url_encode(submodel.id_short) == identifier:
                return submodel

        return None

    # endregion

    # region: idShortPath search

    def get_submodel_from_id_short_path(self, id_short_path, submodel: aas_types.Submodel = None):

        if self.cache:
            if self.id_short_path_cache.exists(id_short_path):
                return self.id_short_path_cache.get(id_short_path)

        split_id_short = id_short_path.split(".")
        print("Length of path: ", len(split_id_short))
        split_id_short = list(reversed(split_id_short))
        print(split_id_short)

        if submodel is None:
            current_lookup = split_id_short.pop()
            lookup_id_short, lookup_index = get_path_part(current_lookup)
            print("lookup_id_short", lookup_id_short)
            print("lookup_index", lookup_index)
            found_submodel = self.get_submodel_by_identifier(lookup_id_short)
            if found_submodel is None:
                print("submodel not found")
                return None
            print("submodel found")
            if len(split_id_short) == 0:
                print("last in line")
                return found_submodel
            else:
                print("looking for submodel elements")
                result_found_submodel_element = self.get_submodel_element_from_id_short_path(split_id_short,
                                                                                             found_submodel)
                if self.cache:
                    self.id_short_path_cache.put(id_short_path, result_found_submodel_element)
                return result_found_submodel_element

        return None

    def get_submodel_element_from_id_short_path(self, id_short_path_list: [str], submodel: aas_types.SubmodelElement):
        current_path = id_short_path_list.pop()
        print("Length of path: ", len(id_short_path_list))
        lookup_id_short, lookup_index = get_path_part(current_path)
        print("lookup_id_short", lookup_id_short)
        print("lookup_index", lookup_index)
        if lookup_id_short is None:
            return None

        if isinstance(submodel, aas_types.SubmodelElementList):
            print("IS submodel element list")
            if lookup_index is None:
                print("No lookup index for Submodel Element List defined.")
                return None
            else:
                if len(id_short_path_list) == 0:
                    print("No more submodel elements")

                    print("Submodel element class: ", submodel.value[lookup_index].__class__)
                    return submodel.value[lookup_index]
                else:
                    print("Submodel elements found")
                    return self.get_submodel_element_from_id_short_path(id_short_path_list, submodel.value[lookup_index])


        if isinstance(submodel, aas_types.SubmodelElementCollection):
            print("IS submodel element collection")
            for submodel_element in submodel.value:
                if submodel_element.id_short == lookup_id_short:
                    print("Found Submodel element", submodel_element.id_short)

                    if len(id_short_path_list) == 0:
                        print("No more submodel elements")

                        print("Submodel element class: ", submodel_element.__class__)
                        return submodel_element
                    else:
                        print("Submodel elements found")
                        return self.get_submodel_element_from_id_short_path(id_short_path_list, submodel_element)

        if isinstance(submodel, aas_types.Submodel):
            print("IS submodel element")
            for submodel_element in submodel.submodel_elements:
                if submodel_element.id_short == lookup_id_short:
                    print("Found Submodel element", submodel_element.id_short)
                    if len(id_short_path_list) == 0:
                        print("No more submodel elements")
                        print("Submodel elements", submodel_element.__class__)
                        return submodel_element
                    else:
                        print("Submodel elements found")
                        return self.get_submodel_element_from_id_short_path(id_short_path_list, submodel_element)

        return None

    # endregion

    # region: error messaging UNFINISHED !
    def generate_response_message(self,
                                  text: str,
                                  code: int = 200,
                                  correlation_id: str = "N/A",
                                  message_type: str = "Undefined",
                                  ):
        if self.debug:
            print("AAS_API response message: ", text)

        messages = {
            "code": code,
            "correlation_id": correlation_id,
            "message_type": message_type,
            "text": text,
            "timestamp": time.time(),
        }

        return messages

    def generate_response_message_not_implemented(self):
        self.generate_response_message(MESSAGES.NOT_IMPLEMENTED)

    # endregion

    # region: timeseries stuff
    def add_record_to_time_series(self, timestamp, cft, cfdt, cfdp, cfer, statusf1, statusf2, alarmf1, alarmf2,
                                  alarmf3, max_record_count: int = 10):
        """
        Add a new record to the TimeSeries submodel.

        :param timestamp: The timestamp of the record (e.g., in UNIX format or ISO 8601)
        :param cft = Circulation fluid temperature => 000Bh
        :param cfdt = Circulation fluid discharge temperature => 0000h
        :param cfdp = Circulation fluid discharge pressure => 0002h
        :param cfer = Circulation fluid electricity resistivity/conductivity => 0003h
        :param statusf1 = Status flag 1 => 0004h
        :param statusf2 = Status flag 2 => 0009h
        :param alarmf1 = Alarm flag 1 => 0005h
        :param alarmf2 = Alarm flag 2 => 0006h
        :param alarmf3 = Alarm flag 3 => 0007h
        """
        # Get the TimeSeries submodel
        time_series_submodel = self.get_submodel_by_identifier("TimeSeries")
        if time_series_submodel is None:
            raise ValueError("TimeSeries submodel does not exist in the environment.")

        # Locate the "Segments" collection
        segments_collection = None

        if isinstance(time_series_submodel, aas_types.Submodel):
            for elem in time_series_submodel.submodel_elements:
                if elem.id_short == "Segments":
                    segments_collection = elem
                    break
        else:
            raise ValueError("TimeSeries submodel does not exist in the environment.")

        if segments_collection is None or not isinstance(segments_collection, aas_types.SubmodelElementCollection):
            raise ValueError("Segments collection not found or invalid in the TimeSeries submodel.")

        # Locate the "InternalSegment" collection within "Segments"
        internal_segment = None
        for elem in segments_collection.value:
            if isinstance(elem, aas_types.SubmodelElementCollection):
                if elem.id_short == "InternalSegment":
                    internal_segment = elem
                    break

        if internal_segment is None or not isinstance(internal_segment, aas_types.SubmodelElementCollection):
            return None

        # Locate the "Records" collection within "InternalSegment"
        records_collection = None
        for elem in internal_segment.value:
            if elem.id_short == "Records":
                records_collection = elem
                break

        if records_collection is None or not isinstance(records_collection, aas_types.SubmodelElementCollection):
            raise ValueError("Records collection not found in InternalSegment.")

        # Create the new Record collection
        new_record = aas_types.SubmodelElementCollection(
            id_short="Record",
            value=[
                aas_types.Property(
                    id_short="Time",
                    description=[
                        aas_types.LangStringTextType(
                            language="de",
                            text="Enthält die Zeit der Momentaufnahme.",
                        ),
                    ],
                    value_type=aas_types.DataTypeDefXSD.LONG,
                    value=str(timestamp),
                ),
                aas_types.Property(
                    id_short="Circulation Fluid Temperature",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(cft),
                ),
                aas_types.Property(
                    id_short="Circulation fluid discharge Temperature",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(cfdt),
                ),
                aas_types.Property(
                    id_short="Circulation fluid discharge pressure",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(cfdp),
                ),
                aas_types.Property(
                    id_short="Circulation fluid electricity resistivity/conductivity",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(cfer),
                ),
                aas_types.Property(
                    id_short="Status flag 1",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(statusf1),
                ),
                aas_types.Property(
                    id_short="Status flag 2",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(statusf2),
                ),
                aas_types.Property(
                    id_short="Alarm flag 1",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(alarmf1),
                ),
                aas_types.Property(
                    id_short="Alarm flag 2",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(alarmf2),
                ),
                aas_types.Property(
                    id_short="Alarm flag 3",
                    value_type=aas_types.DataTypeDefXSD.FLOAT,
                    value=str(alarmf3),
                )
            ]
        )

        if records_collection.value is None:
            return None
        # Add the new record to the "Records" collection
        if len(records_collection.value) > max_record_count:
            records_collection.value.pop()
        records_collection.value.append(new_record)
        print(f"Added new record with timestamp {timestamp} and temperature {cft}.")

    # endregion

    # region: Encoding
    def base64url_encode(self, data: str) -> str:
        # Convert the input string to bytes
        byte_data = data.encode("utf-8")

        # Base64 encode the bytes
        base64_bytes = ubinascii.b2a_base64(byte_data).strip()  # Strip newline

        # Convert Base64 bytes to a string and make it URL-safe
        base64_url = base64_bytes.decode("utf-8").replace("+", "-").replace("/", "_").rstrip("=")

        return base64_url

    # endregion

    # region: Asset Administration Shell
    def get_asset_administration_shell(self, serialization_modifier=None):
        try:
            jsonable = aas_jsonization.to_jsonable(self.aas)
            if self.debug:
                print(MESSAGES.SUCCESS_GET_AAS_ENVIRONMENT)
            return jsonable
        except Exception as e:
            return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e), code=500)

    def put_asset_administration_shell(self, request, serialization_modifier=None):
        try:
            aas_aas = aas_jsonization.asset_administration_shell_from_jsonable(request.body)
            self.aas = aas_aas
            return self.generate_response_message(MESSAGES.SUCCESS_CREATE_AAS_ENVIRONMENT)
        except Exception as e:
            return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e))

    # endregion

    # region: Asset Information
    def get_asset_information(self, request, serialization_modifier=None):
        try:
            # Since we only have one Shell we return the first one
            jsonable = aas_jsonization.to_jsonable(self.aas.asset_administration_shells[0].asset_information)
            if self.debug:
                print(MESSAGES.SUCCESS_GET_ASSET_INFORMATION)
            return jsonable
        except Exception as e:
            return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e), code=500)

    # endregion

    # region: Submodels
    def get_all_submodel_references(self):
        try:
            # Generate submodel references from the Chiller instance
            submodel_refs = []
            for submodel in self.aas.submodels:
                submodel_ref = {
                    "idShort": submodel.id_short,
                    "type": "Submodel",
                    "keys": [
                        {
                            "type": "Submodel",
                            "value": self.base64url_encode(submodel.id)  # Unique ID of the submodel
                        }
                    ]
                }
                submodel_refs.append(submodel_ref)
            json_data = ujson.dumps(submodel_refs).encode('utf-8')
            if self.debug:
                print(MESSAGES.SUCCESS_GET_SUBMODEL_REFS)
            return json_data
        except Exception as e:
            return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e), code=500)

    def get_submodel(self, request, submodel_identifier, serialization_modifier=None):
        """
            Retrieves a submodel from the AAS server based on the provided identifier and optional serialization modifier.

            This method supports different serialization formats through modifiers:
            - $value: Returns only the values of the submodel elements
            - $reference: Returns a reference to the submodel
            - $path: Returns the id_short as a path
            - None: Returns the complete submodel JSON

            Args:
                request: The incoming request object
                submodel_identifier (str): The identifier of the submodel to retrieve
                serialization_modifier (str, optional): Modifier to control the response format.
                    Valid values are "$value", "$reference", "$path", or None. Defaults to None.

            Returns:
                dict/list: The requested submodel data in the specified format. Format depends on serialization_modifier:
                    - dict: Complete submodel JSON (default) or $value format
                    - dict: Reference object for $reference format
                    - list: Path components for $path format
                dict: Error message if the operation fails, with structure:
                    {
                        "message": str,  # Error description
                        "code": int      # HTTP status code
                    }

            Raises:
                No exceptions are raised directly - all errors are returned as response messages

            Example:
                get_submodel(request, "temperature_sensor")
                {<complete submodel JSON>}

                get_submodel(request, "temperature_sensor", "$value")
                {<value-only submodel data>}
            """
        if submodel_identifier is None:
            return self.generate_response_message(MESSAGES.USAGE_GET_SUBMODEL, code=400)
        else:
            submodel_exists = self.does_submodel_exist(submodel_identifier)
            if submodel_exists:
                found_submodel = self.get_submodel_by_identifier(submodel_identifier)
                if self.debug:
                    print("Submodel found by id_short:", found_submodel.id_short)
                if serialization_modifier == "$value":
                    if found_submodel is not None:
                        try:
                            jsonable = aas_jsonization.to_jsonable(found_submodel)

                            return self.convert_to_value_only(jsonable)
                        except Exception as e:
                            return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e), code=500)
                    else:
                        return self.generate_response_message("Submodel was found but has no value")
                if serialization_modifier == "$reference":
                    if found_submodel.id is not None:
                        try:
                            submodel_reference = aas_types.Reference(
                                type=aas_types.ReferenceTypes.MODEL_REFERENCE,
                                keys=[
                                    aas_types.Key(
                                        type=aas_types.KeyTypes.SUBMODEL,
                                        value=found_submodel.id
                                    )
                                ]
                            )
                            jsonable = aas_jsonization.to_jsonable(submodel_reference)
                            if self.debug:
                                print("get_submodel/$value: successfully serialized aas into json")
                            return jsonable
                        except Exception as e:
                            return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e), code=500)
                    else:
                        return self.generate_response_message("Submodel was found but unable to find reference")
                if serialization_modifier == "$path":
                    if found_submodel.id_short is not None:
                        response_json = [
                            found_submodel.id_short
                        ]
                        return response_json
                    else:
                        return self.generate_response_message("Submodel was found but unable to find path")
                jsonable = aas_jsonization.to_jsonable(found_submodel)
                return jsonable
            else:
                response_message = "Submodel was found" if submodel_exists else "Submodel was not found"
                return self.generate_response_message(response_message)

    def put_submodel(self, request, submodel_identifier, serialization_modifier=None):
        if submodel_identifier is None:
            return self.generate_response_message(MESSAGES.USAGE_PUT_SUBMODEL)
        else:
            submodel_exists = self.does_submodel_exist(submodel_identifier)
            if submodel_exists:
                found_submodel = self.get_submodel_by_identifier(submodel_identifier)
                try:
                    # This will fail if it receives a nested json
                    jsonable = ujson.loads(request.body)
                    submodel_to_put = aas_jsonization.submodel_from_jsonable(jsonable)
                    found_submodel = submodel_to_put
                    return self.generate_response_message("Submodel was found and updated successfully.")
                except Exception as e:
                    return self.generate_response_message(MESSAGES.ERROR_JSON_SERIALIZATION + str(e))
            else:
                return {"message": submodel_exists}

    def delete_submodel(self, request, submodel_identifier, serialization_modifier=None):
        if submodel_identifier is None:
            return self.generate_response_message("No submodel name given in path.")
        else:
            submodel_exists = self.does_submodel_exist(submodel_identifier)
            if submodel_exists:
                found_submodel = self.get_submodel_by_identifier(submodel_identifier)
                self.aas.submodels.remove(found_submodel)
                return self.generate_response_message("Submodel was found and deleted successfully.")
            else:
                return self.generate_response_message("Submodel was not found.")

    # endregion

    # region: Submodel Elements
    def get_submodel_element_by_path(self, request, submodel_identifier, id_short_path, serialization_modifier=None):
        if submodel_identifier is None or id_short_path is None:
            return self.generate_response_message(MESSAGES.USAGE_SUBMODEL_ELEMENT)
        else:
            found_by_path = self.get_submodel_from_id_short_path(submodel_identifier + "." + id_short_path)
            if found_by_path:
                if self.debug:
                    print("Submodel found by found_by_path")
                if serialization_modifier == "$value":
                    if isinstance(found_by_path, aas_types.Property):
                        if found_by_path.value is not None:
                            if self.debug:
                                print("Found value:", found_by_path.value)
                            return found_by_path.value
                    # Here is where I would put my ValueOnly methods IF I HAD ANY
                    jsonable = aas_jsonization.to_jsonable(found_by_path)
                    return jsonable
                if serialization_modifier == "$reference":
                    return self.generate_response_message("SubmodelElement lookup with $reference is not implemented")
                if serialization_modifier == "$path":
                    return [id_short_path]

                jsonable = aas_jsonization.to_jsonable(found_by_path)
                return jsonable

    def patch_submodel_element_by_path(self, request, submodel_identifier, id_short_path, serialization_modifier=None):
        if submodel_identifier is None or id_short_path is None:
            return {"message": "please use /aas/submodels/<submodel_identifier>/submodel-elements/<idShortPath>"}
        else:
            found_by_path = self.get_submodel_from_id_short_path(submodel_identifier + "." + id_short_path)
            if found_by_path:
                print("Submodel found by found_by_path")
                if serialization_modifier == "$value":
                    if found_by_path.value is not None:
                        print("x Found value:", found_by_path.value)
                        print(request.body)
                        if request.body and isinstance(found_by_path, aas_types.Property):
                            print("error ?")
                            found_by_path.value = str(request.body)
                            print("no error ?")
                            return self.generate_response_message("Successfully updated property")

                jsonable = aas_jsonization.to_jsonable(found_by_path)
                return jsonable

    # endregion

    # region: Metrics

    def get_metric_json_serialization_speed(self, request):
        # Record the start time in microseconds
        start_time = time.ticks_us()

        # Serialize the JSON
        jsonable = aas_jsonization.to_jsonable(self.aas)
        json_data = ujson.dumps(jsonable).encode('utf-8')
        json_size = len(json_data)

        # Record the end time in microseconds
        end_time = time.ticks_us()

        # Calculate the elapsed time in microseconds
        elapsed_time = time.ticks_diff(end_time, start_time)

        # Return a JSON response with the serialization timestamp and the time it took
        return {
            "metric": "json serialization speed",
            "timestamp": time.ticks_us(),  # Current time in microseconds
            "result": elapsed_time,  # Time taken for serialization in microseconds
            "json_size": json_size
        }

    def get_metric_json_serialization_speed_growing(self, request):
        # Record the start time in microseconds
        self.add_record_to_time_series("0", "0", "0", "0", "0", "0", "0", "0", "0", "0")

        start_time = time.ticks_us()

        # Serialize the JSON
        jsonable = aas_jsonization.to_jsonable(self.aas)
        json_data = ujson.dumps(jsonable).encode('utf-8')
        json_size = len(json_data)

        # Record the end time in microseconds
        end_time = time.ticks_us()

        # Calculate the elapsed time in microseconds
        elapsed_time = time.ticks_diff(end_time, start_time)

        # Return a JSON response with the serialization timestamp and the time it took
        return {
            "metric": "json serialization speed",
            "timestamp": time.ticks_us(),  # Current time in microseconds
            "result": elapsed_time,  # Time taken for serialization in microseconds
            "json_size": json_size
        }

    def get_metric_id_short_path_lookup_speed(self, request, submodel_identifier, id_short_path):
        # Record the start time in microseconds
        start_time = time.ticks_us()

        look_up = self.get_submodel_element_by_path(request, submodel_identifier, id_short_path)

        # Record the end time in microseconds
        end_time = time.ticks_us()

        # Calculate the elapsed time in microseconds
        elapsed_time = time.ticks_diff(end_time, start_time)
        return {
            "metric": "idShortPath lookup speed in us",
            "timestamp": time.ticks_us(),  # Current time in microseconds
            "result": elapsed_time,  # Time taken for serialization in microseconds
            "lookup_success": True if look_up else False
        }
    # endregion


    # region: Helper

    @staticmethod
    def convert_to_value_only(aas_json):
        """
        Tries to convert AAS JSON to ValueOnly notation for MicroPython.

        Args:
            aas_json (dict): The input AAS JSON structure

        Returns:
            dict: The ValueOnly notation JSON hopefully
        """

        def extract_value(json_element):
            model_type = json_element.get("modelType", "")

            if model_type == "Property":
                return json_element.get("value")

            elif model_type == "MultiLanguageProperty":
                values = json_element.get("value", [])
                if values:
                    return values[0].get("text")
                return None

            elif model_type == "SubmodelElementCollection":
                collection_values = {}
                for item in json_element.get("value", []):
                    if "idShort" in item:
                        collection_values[item["idShort"]] = extract_value(item)
                return collection_values

            return None

        result = {}

        elements = aas_json.get("submodelElements", [])
        for element in elements:
            if "idShort" in element:
                result[element["idShort"]] = extract_value(element)

        return result

    # endregion
