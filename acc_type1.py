#!/usr/bin/env python3
from panda import Panda
from opendbc.can.packer import CANPacker

dbc_name ='toyota_nodsu_hybrid_pt_generated'
packer = CANPacker(dbc_name)

if __name__ == "__main__":
    p = Panda()
    p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
    print(p.health())
    # If safety mode == 0, so ALLOUTPUT don't worked

    values = {
      "ACC_TYPE": 1,
    }

    data = packer.make_can_msg("ACC_CONTROL", 0, values)
    print(data)
    while 1:
      p.can_send(data[0], data[2], data[3])

