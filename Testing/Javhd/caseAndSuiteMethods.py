from dotmap import DotMap

DICTIONARY = DotMap(
    {
        # Аттрибуты для тест-сьютов
        'url': 'URL',
        'test_cases': 'test_cases',
        'locator': 'locator',
        'steps': 'steps',

        #  Возможные аттрибуты и действия для тест-кейсов
        'click': 'click',
        'dblclick': 'dblclick',
        'input': 'input',
        'wait': 'wait',
        'compare_url': 'compare_url',
        'enter_event': 'enter_event',
        'tab_event': 'tab_event',
    }
)
