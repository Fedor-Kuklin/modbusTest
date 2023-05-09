from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from pymodbus.pdu import ExceptionResponse
import logging
import serial.tools.list_ports


_logger = logging.getLogger()
logging.basicConfig(level=logging.DEBUG,
                    filename="py_log.log",
                    filemode="w",
                    # format="%(asctime)s %(levelname)s %(message)s"
                    )


_logger.info([f"{comport}: {desc} [{hwid}]" for comport, desc, hwid in sorted(serial.tools.list_ports.comports())])


def client_run():
    client = ModbusSerialClient(port='COM1', baudrate=9600, bytesize=8, parity='N', stopbits=1)
    return client


def client_polls(client, func:str, data_start:int, data_len:int, slave:int):

    match func:
        case '01':
            try:
                rr = client.read_coils(data_start, data_len, slave=slave)
            except ModbusException as exc:
                txt = f"ERROR: exception in pymodbus {exc}"
                _logger.error(txt)
                raise exc
            if rr.isError():
                txt = "ERROR: pymodbus returned an error!"
                _logger.error(txt)
                raise ModbusException(txt)
            if isinstance(rr, ExceptionResponse):
                txt = "ERROR: received exception from device {rr}!"
                _logger.error(txt)
                # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
                raise ModbusException(txt)

            # Validate data
            txt = f"### Template coils response: {str(rr.bits)}"
            _logger.debug(txt)
            print(rr.bits)
            return rr.bits
        case '02':
            try:
                rr = client.read_discrete_inputs(data_start, data_len, slave=slave)
            except ModbusException as exc:
                txt = f"ERROR: exception in pymodbus {exc}"
                _logger.error(txt)
                raise exc
            if rr.isError():
                txt = "ERROR: pymodbus returned an error!"
                _logger.error(txt)
                raise ModbusException(txt)
            if isinstance(rr, ExceptionResponse):
                txt = "ERROR: received exception from device {rr}!"
                _logger.error(txt)
                # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
                raise ModbusException(txt)
            txt = f"### Template coils response: {str(rr.bits)}"
            _logger.debug(txt)
            return txt
        case '03':
            try:
                rr = client.read_holding_registers(data_start, data_len, slave=slave)
            except ModbusException as exc:
                txt = f"ERROR: exception in pymodbus {exc}"
                _logger.error(txt)
                raise exc
            if rr.isError():
                txt = "ERROR: pymodbus returned an error!"
                _logger.error(txt)
                raise ModbusException(txt)
            if isinstance(rr, ExceptionResponse):
                txt = "ERROR: received exception from device {rr}!"
                _logger.error(txt)
                # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
                raise ModbusException(txt)
            txt = f"### Template coils response: {str(rr.registers)}"
            _logger.debug(txt)
            return txt
        case '04':
            try:
                rr = client.read_input_registers(data_start, data_len, slave=slave)
            except ModbusException as exc:
                txt = f"ERROR: exception in pymodbus {exc}"
                _logger.error(txt)
                raise exc
            if rr.isError():
                txt = "ERROR: pymodbus returned an error!"
                _logger.error(txt)
                raise ModbusException(txt)
            if isinstance(rr, ExceptionResponse):
                txt = "ERROR: received exception from device {rr}!"
                _logger.error(txt)
                # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
                raise ModbusException(txt)
            txt = f"### Template coils response: {str(rr.registers)}"
            _logger.debug(txt)
            return txt


def run_sync_polls(client):
    return client_polls(client=client, func='01', data_start=0, data_len=10, slave=3)


def run_sync_client(client, modbus_calls=None):
    """Run sync client."""
    _logger.info("### Client starting")

    client.connect()
    if modbus_calls:
        modbus_calls
    client.close()

    _logger.info("### End of Program")


if __name__ == "__main__":
    testclient = client_run()
    run_sync_client(client=testclient, modbus_calls=run_sync_polls(testclient))
