import json
import os
import matplotlib.pyplot as plt


def load_data(f_name):
    res_x, res_y, res_z = [], [], []
    with open(f_name) as in_f:
        for line in in_f:
            x = json.loads(line)
            res_x += eval(x[1]['AxisX'])
            res_y += eval(x[1]['AxisY'])
            res_z += eval(x[1]['AxisZ'])
    return {
        'x': res_x,
        'y': res_y,
        'z': res_z
    }


def clip(data, start, end):
    return {
        'x': data['x'][start:end],
        'y': data['y'][start:end],
        'z': data['z'][start:end]
    }


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def plot_axis(*args):
    for axis in args:
        plt.plot(axis)
    plt.grid(True)
    plt.show()


def export_file(*args):
    x, y, z, f_name, count = args[0], args[1], args[2], args[3], args[4]

    x_count, y_count, z_count = count, count, count

    path, action, name = f_name

    m_type = "fall" if "fall" in action else "nonfall"

    for fx in x:
        out_name = path + '/' + m_type + '_x_' + action + '_' + name + '_' + str(x_count) + '.txt'
        with open(out_name, 'w') as out_x:
            for f_line in fx:
                out_x.write(str(f_line) + '\n')
        x_count += 1

    for fy in y:
        out_name = path + '/' + m_type + '_y_' + action + '_' + name + '_' + str(y_count) + '.txt'
        with open(out_name, 'w') as out_y:
            for f_line in fy:
                out_y.write(str(f_line) + '\n')
        y_count += 1

    for fz in z:
        out_name = path + '/' + m_type + '_z_' + action + '_' + name + '_' + str(z_count) + '.txt'
        with open(out_name, 'w') as out_z:
            for f_line in fz:
                out_z.write(str(f_line) + '\n')
        z_count += 1


def rename_batch():
    main_dir = "template"
    files = os.listdir(main_dir)
    for each_f in files:
        action = each_f.split(")")[0][6:]
        _, axis, no = each_f.split("_")
        if "fall" not in action:
            new_name = "nonfall_" + action + "_" + axis + "_" + no
            print('template/' + each_f, 'template/' + new_name)
            os.rename(main_dir + '/' + each_f, 'template/' + new_name)
        elif "fall" in action:
            new_name = "fall_" + action + "_" + axis + "_" + no
            print('template/' + each_f, 'template/' + new_name)
            os.rename(main_dir + '/' + each_f, 'template/' + new_name)


def add_name():
    main_dir = "template"
    files = os.listdir(main_dir)
    for each_f in files:
        n_type, action, axis, no = each_f.rsplit("_")
        new_name = n_type + "_" + axis + "_" + action + "_jacky_" + no
        os.rename('template/' + each_f, "template/" + new_name)


def create_directory():
    if not os.path.exists('log'):
        os.mkdir('log')

    if not os.path.exists('template/fall/freefall'):
        os.makedirs('template/fall/freefall')
        os.makedirs('template/fall/forwardfall')
        os.makedirs('template/fall/backwardfall')
        os.makedirs('template/fall/fall2left')
        os.makedirs('template/fall/fall2right')

        os.makedirs('template/nonfall/standing')
        os.makedirs('template/nonfall/running')
        os.makedirs('template/nonfall/walking')
    pass


if __name__ == "__main__":
    """ Step 1, setup file naming """
    in_action = 'walking'
    in_name = 'erik'
    in_f_name = 'e_' + in_action + '.txt'

    """ Step 2, setup operation to perform """
    plot_raw = False
    export = False

    """ Ensure output directory """
    create_directory()
    raw = load_data('log/' + in_f_name)
    clip_data = clip(raw, 0, 0)

    """ Load raw data from text file """
    # raw = load_data('log/walking_jacky.txt')
    # raw = load_data('log/walking_yin.txt')
    # raw = load_data('log/freefall.txt')
    # raw = load_data('log/forwardfall.txt')
    # raw = load_data('log/backwardfall.txt')
    # raw = load_data('log/fall2left.txt')
    # raw = load_data('log/fall2right.txt')
    # raw = load_data('log/standing.txt')
    # raw = load_data('log/running.txt')

    """ erik """
    # raw = load_data('log/e_freefall.txt')
    # raw = load_data('log/e_forwardfall.txt')
    # raw = load_data('log/e_backwardfall.txt')
    # raw = load_data('log/e_fall2left.txt')
    # raw = load_data('log/e_fall2right.txt')
    # raw = load_data('log/e_standing.txt')
    # raw = load_data('log/e_running.txt')
    # raw = load_data('log/e_walking.txt')

    """ Clipping into target range """
    # clip_data = clip(raw, 6000, 16000)  # walking_jacky
    # clip_data = clip(raw, 500, 1300)  # walking_yin
    # clip_data = clip(raw, 2000, ?)  # freefall
    # clip_data = clip(raw, 4200, 8000)  # forwardfall
    # clip_data = clip(raw, 14000, 22000)  # backwardfall
    # clip_data = clip(raw, 0, 7000)  # fall2left
    # clip_data = clip(raw, 8000, 16000)  # fall2right
    # clip_data = clip(raw, 0, 5000)  # standing
    # clip_data = clip(raw, 1000, 5000)  # running

    """ erik """
    # clip_data = clip(raw, 0, 7000)  # freefall_erik
    # clip_data = clip(raw, 0, 7000)  # forwardfall_erik
    # clip_data = clip(raw, 0, 7000)  # backwardfall_erik
    # clip_data = clip(raw, 0, 7000)  # fall2left_erik
    # clip_data = clip(raw, 0, 5400)  # fall2right_erik
    # clip_data = clip(raw, 0, 3500)  # standing_erik
    # clip_data = clip(raw, 0, 2500)  # running_erik
    # clip_data = clip(raw, 0, 5000)  # walking_erik

    """ Partition into n part by 50 each """
    in_type = 'fall' if 'fall' in in_action else 'nonfall'
    if export:
        part_x = chunks(clip_data['x'], 50),
        part_y = chunks(clip_data['y'], 50),
        part_z = chunks(clip_data['z'], 50),
        export_file(
            part_x[0], part_y[0], part_z[0],
            ['template/' + in_type + '/' + in_action, in_action, in_name],
            1
        )
        pass

    """ Plot raw data """
    if plot_raw:
        plot_axis(
            raw['x'],
            raw['y'],
            raw['z'],
        )
        pass

    """ Plot clip data """
    # plot_axis(
    #     clip_data['x'],
    #     clip_data['y'],
    #     clip_data['z'],
    # )

    """ Plot single window """
    # plot_axis(
    #     [x for x in part_x[0]][1],
    #     [x for x in part_y[0]][1],
    #     [x for x in part_z[0]][1],
    # )
    pass
