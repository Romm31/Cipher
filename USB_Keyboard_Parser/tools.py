import subprocess
import sys

class KeyMapping:
    usb_codes = {
        "0x04": ['a', 'A'], "0x05": ['b', 'B'], "0x06": ['c', 'C'], "0x07": ['d', 'D'], "0x08": ['e', 'E'],
        "0x09": ['f', 'F'], "0x0A": ['g', 'G'], "0x0B": ['h', 'H'], "0x0C": ['i', 'I'], "0x0D": ['j', 'J'],
        "0x0E": ['k', 'K'], "0x0F": ['l', 'L'], "0x10": ['m', 'M'], "0x11": ['n', 'N'], "0x12": ['o', 'O'],
        "0x13": ['p', 'P'], "0x14": ['q', 'Q'], "0x15": ['r', 'R'], "0x16": ['s', 'S'], "0x17": ['t', 'T'],
        "0x18": ['u', 'U'], "0x19": ['v', 'V'], "0x1A": ['w', 'W'], "0x1B": ['x', 'X'], "0x1C": ['y', 'Y'],
        "0x1D": ['z', 'Z'], "0x1E": ['1', '!'], "0x1F": ['2', '@'], "0x20": ['3', '#'], "0x21": ['4', '$'],
        "0x22": ['5', '%'], "0x23": ['6', '^'], "0x24": ['7', '&'], "0x25": ['8', '*'], "0x26": ['9', '('],
        "0x27": ['0', ')'], "0x28": ['\n', '\n'], "0x29": ['[ESC]', '[ESC]'], "0x2A": ['[BACKSPACE]', '[BACKSPACE]'],
        "0x2B": ['\t', '\t'], "0x2C": [' ', ' '], "0x2D": ['-', '_'], "0x2E": ['=', '+'], "0x2F": ['[', '{'],
        "0x30": [']', '}'], "0x31": ['\\', '|'], "0x32": ['#', '~'], "0x33": [';', ':'], "0x34": ['\'', '"'],
        "0x36": [',', '<'], "0x37": ['.', '>'], "0x38": ['/', '?'], "0x39": ['[CAPSLOCK]', '[CAPSLOCK]'],
    }

    def __init__(self):
        self.devices = dict()
        self.capslock_active = False

    def register_new_device(self, ip):
        self.devices[ip] = list()

    def _decode_keypress(self, val):
        shift = val[0] == 0x02 or val[0] == 0x20 or val[0] == 0x22  # Left or Right shift
        keycode = "0x" + str(hex(val[0x2]))[2:].zfill(2).upper()
        if keycode in self.usb_codes:
            if self.usb_codes[keycode][0] == '[BACKSPACE]':
                return None
            if self.usb_codes[keycode][0] == '[CAPSLOCK]':
                self.capslock_active = not self.capslock_active
                return None
            char_pair = self.usb_codes[keycode]
            if char_pair[0].isalpha():
                use_upper = shift ^ self.capslock_active
                return char_pair[1] if use_upper else char_pair[0]
            else:
                return char_pair[1] if shift else char_pair[0]
        return None

    def push_result(self, out):
        if out['id'] not in self.devices:
            self.register_new_device(out['id'])
        decoded = self._decode_keypress(out['data'])
        if decoded:
            self.devices[out['id']].append(decoded)

    def dump_result(self):
        return ''.join([item for sublist in self.devices.values() for item in sublist])

class USBKeyboard:
    def __init__(self, filename):
        self.filename = filename
        self.result = KeyMapping()

    def read_pcap(self):
        command = ["tshark", "-r", self.filename, "-Y", "usb.capdata", "-T", "fields", "-e", "usb.capdata"]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.splitlines()

    def decode(self):
        for line in self.read_pcap():
            try:
                raw_data = bytes.fromhex(line.strip())
                if len(raw_data) >= 8:
                    device_id = raw_data[0x1]
                    self.result.push_result({"id": device_id, "data": raw_data})
            except ValueError:
                continue
        return self.result.dump_result()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools.py <file.pcap>")
        sys.exit(1)

    file_path = sys.argv[1]
    usb_keyboard = USBKeyboard(file_path)
    decoded_result = usb_keyboard.decode()
    print("[+] Reconstructed Keystrokes:\n")
    print(decoded_result)
