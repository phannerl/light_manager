from django.shortcuts import render


def light_handle(light_brightness_list_org, expected_brightness_org) -> list[list[int]]:
    # input:  [200, 300, 600, 700], 700
    # output:  [[200, 200, 300], [700]]
    final_result = []
    stack = [(light_brightness_list_org, expected_brightness_org, [])]
    while stack:
        light_brightness_list, expected_brightness, previous_result = stack.pop()
        for i, light_brightness in enumerate(light_brightness_list):
            if light_brightness > expected_brightness:
                continue
            elif light_brightness == expected_brightness:
                if previous_result:
                    final_result += [previous_result +
                                     [light_brightness]]
                else:
                    final_result += [[light_brightness]]
                continue
            else:
                stack.append((light_brightness_list[i:], expected_brightness -
                             light_brightness, previous_result + [light_brightness]))
    return final_result


if __name__ == "__main__":
    light_brightness_list = map(int, input('LightBrightness').split(' '))
    expected_brightness = int(input('expectedBrightness'))
    list_of_light_brightness = sorted(light_brightness_list)
    print(light_handle(list_of_light_brightness, expected_brightness))
