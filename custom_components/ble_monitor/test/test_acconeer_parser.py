"""The tests for the Acconeer ble_parser."""
from ble_monitor.ble_parser import BleParser


class TestAcconeer:
    """Tests for the Acconeer parser"""

    def test_acconeer_xm122(self):
        """Test acconeer parser for Acconeer XM122."""
        data_string = (
            "043e22020103013412b69009e01602010612ffc0ac806400160001000000000000000000c2"
        )

        data = bytes(bytearray.fromhex(data_string))

        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Acconeer"
        assert sensor_msg["type"] == "Acconeer XM122"
        assert sensor_msg["mac"] == "E00990B61234"
        assert sensor_msg["packet"] == "6400160001000000000000000000"
        assert sensor_msg["data"]
        assert sensor_msg["battery"] == 100
        assert sensor_msg["temperature"] == 22
        assert sensor_msg["motion"] == 1
        assert sensor_msg["rssi"] == -62

    def test_acconeer_xm126(self):
        """Test acconeer parser for Acconeer XM126."""
        data_string = (
            "043e22020103013412b69009e01602010612ffc0ac916400160001000000000000000000c2"
        )

        data = bytes(bytearray.fromhex(data_string))

        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Acconeer"
        assert sensor_msg["type"] == "Acconeer XM126"
        assert sensor_msg["mac"] == "E00990B61234"
        assert sensor_msg["packet"] == "6400160001000000000000000000"
        assert sensor_msg["data"]
        assert sensor_msg["battery"] == 100
        assert sensor_msg["temperature"] == 22
        assert sensor_msg["motion"] == 1
        assert sensor_msg["distance mm"] == 0
        assert sensor_msg["rssi"] == -62

    def test_acconeer_xm126_distance(self):
        """Test acconeer parser for Acconeer XM126 Distance."""
        data_string = (
            "043e22020103013412b69009e01602010612ffc0ac906400160058050000000000000000c2"
        )

        data = bytes(bytearray.fromhex(data_string))

        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Acconeer"
        assert sensor_msg["type"] == "Acconeer XM126"
        assert sensor_msg["mac"] == "E00990B61234"
        assert sensor_msg["packet"] == "6400160058050000000000000000"
        assert sensor_msg["data"]
        assert sensor_msg["battery"] == 100
        assert sensor_msg["temperature"] == 22
        assert sensor_msg["distance mm"] == 1368
        assert sensor_msg["rssi"] == -62

    def test_acconeer_xm126_touch(self):
        """Test acconeer parser for Acconeer XM126 Touchless Button."""
        data_string = (
            "043e22020103013412b69009e01602010612ffc0ac9564001800010001008a0904000000c2"
        )

        data = bytes(bytearray.fromhex(data_string))

        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Acconeer"
        assert sensor_msg["type"] == "Acconeer XM126"
        assert sensor_msg["mac"] == "E00990B61234"
        assert sensor_msg["packet"] == "64001800010001008a0904000000"
        assert sensor_msg["data"]
        assert sensor_msg["battery"] == 100
        assert sensor_msg["temperature"] == 24
        assert sensor_msg["distance mm"] == 2442
        assert sensor_msg["distance"] == 4
        assert sensor_msg["button"] == 0
        assert sensor_msg["rssi"] == -62

        data_string = (
            "043e22020103013412b69009e01602010612ffc0ac956400180002000000000000000100c2"
        )

        data = bytes(bytearray.fromhex(data_string))

        # pylint: disable=unused-variable
        ble_parser = BleParser()
        sensor_msg, tracker_msg = ble_parser.parse_raw_data(data)

        assert sensor_msg["firmware"] == "Acconeer"
        assert sensor_msg["type"] == "Acconeer XM126"
        assert sensor_msg["mac"] == "E00990B61234"
        assert sensor_msg["packet"] == "6400180002000000000000000100"
        assert sensor_msg["data"]
        assert sensor_msg["battery"] == 100
        assert sensor_msg["temperature"] == 24
        assert sensor_msg["distance mm"] == 0
        assert sensor_msg["distance"] == 0
        assert sensor_msg["button"] == 1
        assert sensor_msg["rssi"] == -62
