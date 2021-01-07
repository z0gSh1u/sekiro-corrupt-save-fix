# Main fixer of sekiro-corrupt-save-fix
# https://github.com/z0gSh1u/sekiro-corrupt-save-fix

import hashlib
import os.path as path
import shutil

CHECKSUM_SIZE = 0x10  # bytes
RECORD_SIZE = 0x100000  # bytes
CHECKSUM_BASE = 0x00000300  # slot 0
RECORD_BASE = 0x00000310  # slot 0


def get_range(slot_index: int):
    """Calculate checksum and record ranges for certain slot.

    Args:
        slot_index (int): Index of slot. 0-based.

    Returns:
        tuple: (checksum_left, checksum_right, block_left, block_right). Left closed, right closed.
    """
    checksum_left = CHECKSUM_BASE + (CHECKSUM_SIZE + RECORD_SIZE) * slot_index
    checksum_right = checksum_left + CHECKSUM_SIZE - 1
    block_left = checksum_right + 1
    block_right = block_left + RECORD_SIZE - 1

    # [ for debug ]
    # print(
    #     list(map(hex,
    #              (checksum_left, checksum_right, block_left, block_right))))

    return (checksum_left, checksum_right, block_left, block_right)


def backup(sl2_path: str):
    """Backup sl2 file to the directory of sl2_path.

    Args:
        sl2_path (str): Path of Sekiro sl2 save file.
    """
    backup_filename = path.basename(sl2_path) + '.fixbackup'
    backup_savepath = path.join(path.dirname(sl2_path), './', backup_filename)
    shutil.copyfile(sl2_path, backup_savepath)


def fix(sl2_path: str, slot_index: int):
    """Fix the corrupt save by re-calculating the checksum.

    Args:
        sl2_path (str): Path of Sekiro sl2 save file.
        slot_index (int): Index of slot. 0-based.
    """

    (checksum_left, checksum_right, block_left,
     block_right) = get_range(slot_index)

    new_content = b''

    with open(sl2_path, 'rb+') as fp:
        # read range [start] -> [checksum]
        new_content = fp.read(checksum_left)

        # calculate new checksum
        fp.seek(block_left, 0)
        game_record = fp.read(block_right - block_left + 1)
        assert len(game_record) == RECORD_SIZE, 'Bad game save file. No enough game record.'
        new_checksum = hashlib.md5(game_record).digest()

        # concat new checksum
        new_content += new_checksum

        # concat the rest
        fp.seek(block_left, 0)
        new_content += fp.read()

        # overwrite the save
        fp.seek(0)
        fp.write(new_content)


def main(sl2_path: str, slot_index: int):
    # check input format
    assert len(sl2_path) > 0, 'Save file path not specified.'
    assert path.basename(sl2_path) == 'S0000.sl2', 'Selected file is not S0000.sl2.'
    assert slot_index >= 0, 'Invalid slot index.'
    assert slot_index <= 9, 'Invalid slot index.'

    # backup the save
    backup(sl2_path)
    print('The corrupt save has been backup with external name .fixbackup.')

    # fix the save
    print('Start fixing {} @ slot {}.'.format(sl2_path, slot_index))
    fix(sl2_path, slot_index)
    print('Fixing done successfully!')
