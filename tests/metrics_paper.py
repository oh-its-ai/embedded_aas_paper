import sys
import unittest
import os
import psutil
import time
import matplotlib.pyplot as plt
from pympler import asizeof
from aas_core3.jsonization import to_jsonable

from aas_api.aas_api import AasApi
from aas_templates.chiller import Chiller
from aas_templates.performance_env import PerformanceEnv
from types import ModuleType, FunctionType
from gc import get_referents
BLACKLIST = type, ModuleType, FunctionType


class TestMetrics(unittest.TestCase):

    start_submodels = 0
    end_submodels = 100
    step_size = 1

    def getsize(self, obj):
        """sum size of object & members."""
        if isinstance(obj, BLACKLIST):
            raise TypeError('getsize() does not take argument of type: ' + str(type(obj)))
        seen_ids = set()
        size = 0
        objects = [obj]
        while objects:
            need_referents = []
            for obj in objects:
                if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                    seen_ids.add(id(obj))
                    size += sys.getsizeof(obj)
                    need_referents.append(obj)
            objects = get_referents(*need_referents)
        return size
    def setUp(self):
        # Any setup needed before each test
        pass

    def test_json_serialization_speed_ms(self):
        # make X requests to the endpoint: 192.168.0.50/metrics/jsonSerialize
        """
        per request you get:
         {
            "metric": "json serialization speed",
            "timestamp": time.ticks_us(),  # Current time in microseconds
            "result": elapsed_time,  # Time taken for serialization in microseconds
            "json_size": json_size
        }
        please measure the result for over X attemps and display in a bar diagram
        """
        import requests
        import time
        import matplotlib.pyplot as plt
        from statistics import mean, median, stdev

        # Configuration
        endpoint = "http://192.168.0.50/metrics/jsonSerialize"
        num_requests = 50  # Number of requests to make

        # Make requests and collect data
        results = []
        sizes = []

        print(f"Making {num_requests} requests to {endpoint}...")

        for i in range(num_requests):
            try:
                response = requests.get(endpoint)
                if response.status_code == 200:
                    data = response.json()
                    # Convert microseconds to milliseconds
                    results.append(data["result"] / 1000)
                    sizes.append(data["json_size"])
                    print(f"Request {i + 1}/{num_requests}: {results[-1]:.2f} ms, Size: {sizes[-1]} bytes")
                else:
                    print(f"Request {i + 1} failed with status code {response.status_code}")
            except Exception as e:
                print(f"Request {i + 1} failed with error: {str(e)}")

            # Small delay between requests to avoid overwhelming the server
            time.sleep(0.1)

        # Calculate statistics
        if results:
            avg_time = mean(results)
            med_time = median(results)
            if len(results) > 1:
                std_time = stdev(results)
            else:
                std_time = 0
            avg_size = mean(sizes) if sizes else 0

            print(f"\nStatistics:")
            print(f"  Average time: {avg_time:.2f} ms")
            print(f"  Median time: {med_time:.2f} ms")
            print(f"  Standard deviation: {std_time:.2f} ms")
            print(f"  Average JSON size: {avg_size:.2f} bytes")

            # Create visualization
            plt.figure(figsize=(12, 6))

            # Create bar chart of all results
            plt.subplot(1, 2, 1)
            plt.bar(range(len(results)), results, color='skyblue')
            plt.title('JSON Serialization Time per Request')
            plt.xlabel('Request Number')
            plt.ylabel('Time (ms)')
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Create histogram of results
            plt.subplot(1, 2, 2)
            plt.hist(results, bins=10, color='lightgreen', edgecolor='black')
            plt.title('Distribution of Serialization Times')
            plt.xlabel('Time (ms)')
            plt.ylabel('Frequency')
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            plt.tight_layout()
            plt.savefig('json_serialization_results.png')
            plt.show()

        self.assertTrue(True)

    def test_json_serialization_speed_ms_growing_aas(self):
        """
        make X requests to the endpoint: 192.168.0.50/metrics/jsonSerialize
        and measures serialisation speed in milliseconds
        """
        import requests
        import time
        import matplotlib.pyplot as plt
        from statistics import mean, median, stdev

        # Configuration
        endpoint = "http://192.168.0.50/metrics/jsonSerializeGrowing"
        num_requests = 50  # Number of requests to make

        # Make requests and collect data
        results = []
        sizes = []

        print(f"Making {num_requests} requests to {endpoint}...")

        for i in range(num_requests):
            try:
                response = requests.get(endpoint)
                if response.status_code == 200:
                    data = response.json()
                    # Convert microseconds to milliseconds
                    results.append(data["result"] / 1000)
                    sizes.append(data["json_size"])
                    print(f"Request {i + 1}/{num_requests}: {results[-1]:.2f} ms, Size: {sizes[-1]} bytes")
                else:
                    print(f"Request {i + 1} failed with status code {response.status_code}")
            except Exception as e:
                print(f"Request {i + 1} failed with error: {str(e)}")

            # Small delay between requests to avoid overwhelming the server
            time.sleep(0.1)

        # Calculate statistics
        if results:
            avg_time = mean(results)
            med_time = median(results)
            if len(results) > 1:
                std_time = stdev(results)
            else:
                std_time = 0
            avg_size = mean(sizes) if sizes else 0

            print(f"\nStatistics:")
            print(f"  Average time: {avg_time:.2f} ms")
            print(f"  Median time: {med_time:.2f} ms")
            print(f"  Standard deviation: {std_time:.2f} ms")
            print(f"  Average JSON size: {avg_size:.2f} bytes")

            # Create visualization
            plt.figure(figsize=(12, 6))

            # Create bar chart of all results
            plt.subplot(1, 2, 1)
            plt.bar(range(len(results)), results, color='skyblue')
            plt.title('JSON Serialization Time per Request')
            plt.xlabel('Request Number')
            plt.ylabel('Time (ms)')
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Create histogram of results
            plt.subplot(1, 2, 2)
            plt.hist(results, bins=10, color='lightgreen', edgecolor='black')
            plt.title('Distribution of Serialization Times')
            plt.xlabel('Time (ms)')
            plt.ylabel('Frequency')
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            plt.tight_layout()
            plt.savefig('json_serialization_results.png')
            plt.show()

        self.assertTrue(True)

    def test_aas_request_full_response_time_ms(self):
        """
        this test makes X requests to the endpoint: 192.168.0.50/api/v3.0/aas
        measure the time taken for the request and response and plot it in a bar diagram
        """
        import requests
        import time
        import matplotlib.pyplot as plt
        from statistics import mean, median, stdev

        # Configuration
        #endpoint = "http://192.168.0.50/api/v3.0/aas"
        endpoint = "http://192.168.4.1/api/v3.0/aas"
        num_requests = 100  # Number of requests to make

        # Make requests and collect response times
        response_times = []

        print(f"Making {num_requests} requests to {endpoint}...")

        for i in range(num_requests):
            try:
                start_time = time.time()
                response = requests.get(endpoint)
                end_time = time.time()

                # Calculate time in milliseconds
                response_time_ms = (end_time - start_time) * 1000

                if response.status_code == 200:
                    response_times.append(response_time_ms)
                    print(f"Request {i + 1}/{num_requests}: {response_time_ms:.2f} ms")
                else:
                    print(f"Request {i + 1} failed with status code {response.status_code}")
            except Exception as e:
                print(f"Request {i + 1} failed with error: {str(e)}")

            # Small delay between requests to avoid overwhelming the server
            time.sleep(0.2)

        # Calculate statistics
        if response_times:
            avg_time = mean(response_times)
            med_time = median(response_times)
            if len(response_times) > 1:
                std_time = stdev(response_times)
            else:
                std_time = 0

            print(f"\nStatistics:")
            print(f"  Average response time: {avg_time:.2f} ms")
            print(f"  Median response time: {med_time:.2f} ms")
            print(f"  Standard deviation: {std_time:.2f} ms")
            print(f"  Fastest response: {min(response_times):.2f} ms")
            print(f"  Slowest response: {max(response_times):.2f} ms")

            # Create visualization
            plt.figure(figsize=(12, 6))

            # Create bar chart of all response times
            plt.subplot(1, 2, 1)
            plt.bar(range(len(response_times)), response_times, color='skyblue')
            plt.axhline(y=avg_time, color='r', linestyle='-', label=f'Avg: {avg_time:.2f} ms')
            plt.title('AAS API Response Time per Request')
            plt.xlabel('Request Number')
            plt.ylabel('Response Time (ms)')
            plt.legend()
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            # Create histogram of response times
            plt.subplot(1, 2, 2)
            plt.hist(response_times, bins=10, color='lightgreen', edgecolor='black')
            plt.axvline(x=avg_time, color='r', linestyle='-', label=f'Avg: {avg_time:.2f} ms')
            plt.title('Distribution of Response Times')
            plt.xlabel('Response Time (ms)')
            plt.ylabel('Frequency')
            plt.legend()
            plt.grid(axis='y', linestyle='--', alpha=0.7)

            plt.tight_layout()
            plt.savefig('aas_response_times.png')
            plt.show()

        self.assertTrue(True)

    def test_measure_json_serialization_with_chiller_size(self):
        """
        Measure separately:
          - Memory usage for creating a Chiller (in bytes)
          - Memory usage for creating the JSONable representation (in bytes)
          - Creation time for the Chiller (in ms)
          - Serialization time for the JSONable (in ms)

        We'll vary the number of submodels added to the Chiller and plot:
          1) Two memory usage lines (Chiller vs. JSONable) on the left y-axis
          2) Two timing lines (Chiller creation time vs. JSONable serialization time) on the right y-axis
        """


        process = psutil.Process(os.getpid())

        # Range of submodel counts to test
        start_submodels = self.start_submodels
        end_submodels = self.end_submodels
        step_size = self.step_size
        submodel_counts = range(start_submodels, end_submodels + 1, step_size)

        # Arrays for plotting
        chiller_mem_usages_bytes = []      # memory used by the Chiller itself
        jsonable_mem_usages_bytes = []     # incremental memory used by the JSONable structure
        chiller_create_times_ms = []       # time to create & populate Chiller
        jsonable_serialize_times_ms = []   # time to create the JSONable representation

        for submodel_count in submodel_counts:
            # ------------------------------
            # 1) Measure Chiller creation
            # ------------------------------
            mem_before_chiller = process.memory_info().rss
            t_start_chiller = time.time()

            # Create a Chiller with N submodels
            chiller = PerformanceEnv()
            for i in range(submodel_count):
                chiller.addSubmodel()
            print(f"Submodels post adding: {chiller.getSubmodelCount()}\n")
            t_end_chiller = time.time()
            mem_after_chiller = process.memory_info().rss

            chiller_mem_diff = mem_after_chiller - mem_before_chiller
            chiller_create_time_sec = t_end_chiller - t_start_chiller

            # ------------------------------
            # 2) Measure JSONable creation
            # ------------------------------
            t_start_jsonable = time.time()
            jsonable = to_jsonable(chiller)  # Serialize to JSONable
            t_end_jsonable = time.time()

            mem_after_jsonable = process.memory_info().rss
            jsonable_mem_diff = mem_after_jsonable - mem_after_chiller
            jsonable_serialize_time_sec = t_end_jsonable - t_start_jsonable

            # ------------------------------
            # Store the measured values
            # ------------------------------
            chiller_mem_size = self.getsize(chiller)
            chiller_mem_usages_bytes.append(chiller_mem_size)
            json_mem_size = self.getsize(jsonable)
            jsonable_mem_usages_bytes.append(json_mem_size)

            chiller_create_times_ms.append(chiller_create_time_sec * 1000)
            jsonable_serialize_times_ms.append(jsonable_serialize_time_sec * 1000)

            # Print diagnostics
            print(
                f"Submodels: {submodel_count}\n"
                f"  Chiller memory usage: {chiller_mem_size} bytes\n"
                f"  JSONable memory usage: {json_mem_size} bytes\n"
                f"  JSON / AAS memory usage ratio: {json_mem_size / chiller_mem_size} bytes\n"
                f"  Chiller creation time: {chiller_create_time_sec*1000:.2f} ms\n"
                f"  Serialization time: {jsonable_serialize_time_sec*1000:.2f} ms\n"
            )

        # ------------------------------------------------------
        # Plot memory usage (left y-axis) & times (right y-axis)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # Plot 1: Memory usage vs. Submodel count
        # ------------------------------------------------------
        plt.figure(figsize=(8, 5))
        plt.plot(
            submodel_counts,
            chiller_mem_usages_bytes,
            marker='o',
            label='Chiller Memory (MB)'
        )
        plt.plot(
            submodel_counts,
            jsonable_mem_usages_bytes,
            marker='^',
            label='JSONable Memory (MB)'
        )
        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Memory Usage (MB)')
        plt.title("Chiller & JSONable Memory Usage vs. Submodel Count")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        # ------------------------------------------------------
        # Plot 2: Creation & Serialization Time vs. Submodel count
        # ------------------------------------------------------
        plt.figure(figsize=(8, 5))
        plt.plot(
            submodel_counts,
            chiller_create_times_ms,
            marker='s',
            label='Chiller Creation Time (ms)'
        )
        plt.plot(
            submodel_counts,
            jsonable_serialize_times_ms,
            marker='x',
            label='JSONable Serialization Time (ms)'
        )
        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Time (ms)')
        plt.title("Chiller Creation & JSONable Serialization Time vs. Submodel Count")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        self.assertTrue(True)

    def test_measure_json_serialization_with_chiller_size_precreate_aas(self):
        """
        Measure separately:
          - Memory usage for creating a Chiller (in bytes)
          - Memory usage for creating the JSONable representation (in bytes)
          - Creation time for the Chiller (in ms)
          - Serialization time for the JSONable (in ms)

        We'll vary the number of submodels added to the Chiller and plot:
          1) Two memory usage lines (Chiller vs. JSONable) on the left y-axis
          2) Two timing lines (Chiller creation time vs. JSONable serialization time) on the right y-axis

        Now changed so that we pre-create all the Chillers first, then measure serialization
        separately, to avoid intermixed creation/serialization in the same loop.
        """

        process = psutil.Process(os.getpid())

        # Range of submodel counts to test
        start_submodels = self.start_submodels
        end_submodels = self.end_submodels
        step_size = self.step_size
        submodel_counts = range(start_submodels, end_submodels + 1, step_size)

        # Arrays for plotting
        chiller_mem_usages_bytes = []  # Memory used by the Chiller itself
        chiller_create_times_ms = []  # Time to create & populate Chiller

        jsonable_mem_usages_bytes = []  # Memory used by the JSONable structure
        jsonable_serialize_times_ms = []  # Time to create the JSONable representation

        # ----------------------------------------------------
        # 1) PASS: Create all chillers of varying submodel size
        # ----------------------------------------------------
        chillers = []
        for submodel_count in submodel_counts:
            mem_before_chiller = process.memory_info().rss
            t_start_chiller = time.time()

            # Create a Chiller with N submodels
            chiller = PerformanceEnv()
            for i in range(submodel_count):
                chiller.addSubmodel()

            t_end_chiller = time.time()
            mem_after_chiller = process.memory_info().rss

            chiller_mem_diff = mem_after_chiller - mem_before_chiller
            chiller_create_time_sec = t_end_chiller - t_start_chiller

            # Measure memory usage specifically of the chiller object
            chiller_mem_size = self.getsize(chiller)

            chiller_mem_usages_bytes.append(chiller_mem_size)
            chiller_create_times_ms.append(chiller_create_time_sec * 1000)

            # Store the newly created chiller for later serialization
            chillers.append(chiller)

            print(
                f"[CREATION] Submodels: {submodel_count}\n"
                f"  Incremental Process Memory Change: {chiller_mem_diff} bytes\n"
                f"  Chiller object size via getsize(): {chiller_mem_size} bytes\n"
                f"  Chiller creation time: {chiller_create_time_sec * 1000:.2f} ms\n"
            )

        # -----------------------------------------------------------------------
        # 2) PASS: For each pre-created Chiller, measure JSONable serialization
        # -----------------------------------------------------------------------
        for idx, chiller in enumerate(chillers):
            submodel_count = submodel_counts[idx]

            mem_before_jsonable = process.memory_info().rss
            t_start_jsonable = time.time()

            # Serialize to JSONable
            jsonable = to_jsonable(chiller)

            t_end_jsonable = time.time()
            mem_after_jsonable = process.memory_info().rss

            jsonable_mem_diff = mem_after_jsonable - mem_before_jsonable
            jsonable_serialize_time_sec = t_end_jsonable - t_start_jsonable

            # Measure the memory usage of the resultant JSONable structure
            json_mem_size = self.getsize(jsonable)

            jsonable_mem_usages_bytes.append(json_mem_size)
            jsonable_serialize_times_ms.append(jsonable_serialize_time_sec * 1000)

            print(
                f"[SERIALIZATION] Submodels: {submodel_count}\n"
                f"  Incremental Process Memory Change: {jsonable_mem_diff} bytes\n"
                f"  JSONable object size via getsize(): {json_mem_size} bytes\n"
                f"  Serialization time: {jsonable_serialize_time_sec * 1000:.2f} ms\n"
            )

        # ------------------------------------------------------
        # 3) Plot memory usage (left y-axis) & times (right y-axis)
        # ------------------------------------------------------
        # ------------------------------------------------------
        # Plot 1: Memory usage vs. Submodel count
        # ------------------------------------------------------
        plt.figure(figsize=(8, 5))
        plt.plot(
            submodel_counts,
            chiller_mem_usages_bytes,
            marker='o',
            label='Chiller Memory (MB)'
        )
        plt.plot(
            submodel_counts,
            jsonable_mem_usages_bytes,
            marker='^',
            label='JSONable Memory (MB)'
        )
        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Memory Usage (MB)')
        plt.title("Chiller & JSONable Memory Usage vs. Submodel Count (aas pre-created)")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        # ------------------------------------------------------
        # Plot 2: Creation & Serialization Time vs. Submodel count
        # ------------------------------------------------------
        plt.figure(figsize=(8, 5))
        plt.plot(
            submodel_counts,
            chiller_create_times_ms,
            marker='s',
            label='Chiller Creation Time (ms)'
        )
        plt.plot(
            submodel_counts,
            jsonable_serialize_times_ms,
            marker='x',
            label='JSONable Serialization Time (ms)'
        )
        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Time (ms)')
        plt.title("Chiller Creation & JSONable Serialization Time vs. Submodel Count")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        self.assertTrue(True)

    def test_measure_id_short_lookup_speed(self):

        # Range of submodel counts to test
        start_depth = 1
        end_depth = 100 #self.end_submodels
        step_size = 1
        depth_steps = range(start_depth, end_depth + 1, step_size)

        # Arrays for plotting
        chiller_create_times_ms = []  # Time to create & populate Chiller
        idshort_lookup_times_ms = []  # Time to do repeated idShort lookups

        for depth_step in depth_steps:
            print("Depth step:", depth_step)
            # ------------------------------
            # 1) Measure Chiller creation
            # ------------------------------
            t_start_chiller = time.time()

            chiller = PerformanceEnv()

            chiller.add_submodel_element_with_depth(depth_step)
            jsonable = to_jsonable(chiller)
            print("Json: " + str(jsonable))

            t_end_chiller = time.time()
            create_time_ms = (t_end_chiller - t_start_chiller) * 1000
            chiller_create_times_ms.append(create_time_ms)

            # ------------------------------
            # 2) Measure idShort lookup
            # ------------------------------

            aas_api = AasApi(chiller)


            id_short_path_to_find = "TechnicalProperties."
            for i in range(depth_step):
                id_short_path_to_find = id_short_path_to_find + ".SE_DEPTH_" + str(i+1)
            print(id_short_path_to_find)

            t_start_lookup = time.time()
            found_submodel = aas_api.get_submodel_element_by_path(request=None,
                                                  submodel_identifier="TechnicalData",
                                                id_short_path=id_short_path_to_find)

            t_end_lookup = time.time()
            lookup_time_ms = (t_end_lookup - t_start_lookup) * 1000
            idshort_lookup_times_ms.append(lookup_time_ms)

            # Print diagnostics
            print(
                f"[Submodels: {depth_step}]\n"
                f"  Creation Time:       {create_time_ms:.2f} ms\n"
                f"  idShort Lookup Time: {lookup_time_ms:.2f} ms\n"
            )

        # ------------------------------------------------------
        # Plot 1: Chiller Creation Time vs. Submodel count
        # ------------------------------------------------------
        plt.figure(figsize=(8, 5))
        plt.plot(
            depth_steps,
            chiller_create_times_ms,
            marker='o',
            label='Chiller Creation Time (ms)'
        )
        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Time (ms)')
        plt.title("Chiller Creation Time vs. Submodel Count")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        # ------------------------------------------------------
        # Plot 2: idShort Lookup Time vs. Submodel count
        # ------------------------------------------------------
        plt.figure(figsize=(8, 5))
        plt.plot(
            depth_steps,
            idshort_lookup_times_ms,
            marker='^',
            label='idShort Lookup Time (ms)'
        )
        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Time (ms)')
        plt.title("idShort Lookup Time vs. Submodel Count")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        # A simple True assertion so the test runner doesn't fail
        self.assertTrue(True)

    def test_measure_id_short_lookup_speed_randomized(self):

        # Range of submodel counts to test
        start_depth = 1
        end_depth = 850
        step_size = 10
        depth_steps = range(start_depth, end_depth + 1, step_size)

        # Arrays for plotting
        idshort_lookup_times_cached_ms = []  # Time to create & populate Chiller
        idshort_lookup_times_ms = []  # Time to do repeated idShort lookups
        chiller = PerformanceEnv()
        aas_api_cached = AasApi(chiller)
        for depth_step in depth_steps:
            print("Depth step:", depth_step)
            # ------------------------------
            # 1) Measure Chiller creation
            # ------------------------------

            chiller.add_submodel_element_with_depth(depth_step)
            aas_api = AasApi(chiller)
            # ------------------------------
            # 2) Measure idShort lookup
            # ------------------------------




            id_short_path_to_find = "TechnicalProperties"
            for i in range(depth_step):
                id_short_path_to_find = id_short_path_to_find + ".SE_DEPTH_" + str(i+1)
            print(id_short_path_to_find)

            t_start_lookup = time.time()
            found_submodel = aas_api.get_submodel_element_by_path(request=None,
                                                  submodel_identifier="TechnicalData",
                                                id_short_path=id_short_path_to_find)


            t_end_lookup = time.time()

            lookup_time_ms = (t_end_lookup - t_start_lookup) * 1000
            idshort_lookup_times_ms.append(lookup_time_ms)

            t_start_lookup = time.time()
            found_submodel = aas_api_cached.get_submodel_element_by_path(request=None,
                                                                  submodel_identifier="TechnicalData",
                                                                  id_short_path=id_short_path_to_find)


            t_end_lookup = time.time()

            lookup_time_ms = (t_end_lookup - t_start_lookup) * 1000
            idshort_lookup_times_cached_ms.append(lookup_time_ms)
            # Print diagnostics
            print(
                f"[Submodels: {depth_step}]\n"
                f"  idShort Lookup Time: {lookup_time_ms:.2f} ms\n"
            )

        # ------------------------------------------------------

        plt.figure(figsize=(8, 5))
        plt.plot(
            depth_steps,
            idshort_lookup_times_ms,
            marker='^',
            label='idShort Lookup Time (ms)'
        )

        plt.plot(
            depth_steps,
            idshort_lookup_times_cached_ms,
            marker='x',
            label='idShort Lookup Time cached (ms)'
        )

        plt.xlabel('Number of Submodels in Chiller')
        plt.ylabel('Time (ms)')
        plt.title("idShort Lookup Time vs. Submodel Count")
        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        plt.show()

        # A simple True assertion so the test runner doesn't fail
        self.assertTrue(True)