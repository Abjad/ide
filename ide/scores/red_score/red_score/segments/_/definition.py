import abjad


time_signatures = [(15, 8), (18, 8)]
rh_divisions = []
rh_divisions.extend(4 * [(3, 8)])
rh_divisions.extend(4 * [(3, 16)])
rh_divisions.extend(6 * [(5, 16)])
lh_divisions = []
lh_divisions.extend(6 * [(5, 16)])
lh_divisions.extend(4 * [(3, 8)])
lh_divisions.extend(4 * [(3, 16)])
divisions = {
    'RH Voice': rh_divisions,
    'LH Voice': lh_divisions,
    }

maker = abjad.PianoStaffSegmentMaker(
    time_signatures=time_signatures,
    divisions=divisions,
    )
