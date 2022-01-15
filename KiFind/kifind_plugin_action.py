import pcbnew
import re

__version__ = "0.0.1"

board = pcbnew.GetBoard()

def GetUnit(value, do_mm=True):
    if do_mm:
        return pcbnew.ToMM(value)
    else:
        return round(pcbnew.ToMils(value))

def FindAll(board=None, do_tracks=True, do_mm=True):
    if board is None:
        board = GetBoard()    

    results = {}

    for track in board.GetTracks():
        if track.GetClass() in ["TRACK", "VIA"]:
            if do_tracks:
                if track.GetClass() != "TRACK":
                    continue
                s = "{}".format(GetUnit(track.GetWidth(), do_mm))                
            else:
                if track.GetClass() != "VIA":
                    continue
                s = "{}/{}".format(GetUnit(track.GetWidth(), do_mm), GetUnit(track.GetDrillValue(), do_mm))
            if results.get(s) is None:
                results[s] = 1
            else:
                results[s] += 1

    #for key, value in results.items():
    #    print(key + " " + str(value))
    
    return results
    
def DoSelect(board=None, do_tracks=True, do_mm=True, value=""):  
    num = 0
    for track in board.GetTracks():
        if track.GetClass() in ["TRACK", "VIA"]:
            if do_tracks:
                if track.GetClass() != "TRACK":
                    track.ClearSelected()
                    continue
                s = "{}".format(GetUnit(track.GetWidth(), do_mm))
            else:
                if track.GetClass() != "VIA":
                    track.ClearSelected()
                    continue
                s = "{}/{}".format(GetUnit(track.GetWidth(), do_mm), GetUnit(track.GetDrillValue(), do_mm))
            if s == value:
                track.SetSelected()
                num = num + 1
            else:
                track.ClearSelected()
    return num
