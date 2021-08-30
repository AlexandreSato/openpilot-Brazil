#!/usr/bin/env python3
from panda import Panda
from opendbc.can.packer import CANPacker

dbc_name ='toyota_nodsu_hybrid_pt_generated'
packer = CANPacker(dbc_name)

if __name__ == "__main__":
    p = Panda()
    p.set_safety_mode(Panda.SAFETY_ALLOUTPUT)
    dumpsafety = p.health()
    print(f"\nsafety_mode: {dumpsafety['safety_mode']}")
    print("If safety mode == 0? so ALLOUTPUT don't worked OR FLAG ALLOWDEBUG is missing\non Panda flash")

    values = {
      "ACC_TYPE": 1,
    }

    data = packer.make_can_msg("ACC_CONTROL", 0, values)
   
    while 1:
      p.can_send(data[0], data[2], data[3])
      print(data)
