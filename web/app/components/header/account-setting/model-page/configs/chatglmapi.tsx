import { ProviderEnum } from '../declarations'
import type { ProviderConfig } from '../declarations'
import { Chatglm, ChatglmText } from '@/app/components/base/icons/src/public/llm'

const config: ProviderConfig = {
  selector: {
    name: {
      'en': 'ChatGLM Api',
      'zh-Hans': 'ChatGLM Api',
    },
    icon: <Chatglm className='w-full h-full' />,
  },
  item: {
    key: ProviderEnum.chatglmapi,
    titleIcon: {
      'en': <ChatglmText className='h-6' />,
      'zh-Hans': <ChatglmText className='h-6' />,
    },
    disable: {
      tip: {
        'en': 'Only supports the ',
        'zh-Hans': '仅支持',
      },
      link: {
        href: {
          'en': 'https://docs.dify.ai/getting-started/install-self-hosted',
          'zh-Hans': 'https://docs.dify.ai/v/zh-hans/getting-started/install-self-hosted',
        },
        label: {
          'en': 'community open-source version',
          'zh-Hans': '社区开源版本',
        },
      },
    },
  },
  modal: {
    key: ProviderEnum.chatglmapi,
    title: {
      'en': 'ChatGLM',
      'zh-Hans': 'ChatGLM Api',
    },
    icon: <Chatglm className='h-6' />,
    link: {
      href: 'https://open.bigmodel.cn/',
      label: {
        'en': 'Get your API key from ChatGLM',
        'zh-Hans': '从智谱获取APIkey',
      },
    },
    validateKeys: ['api_key'],
    fields: [
      {
        type: 'text',
        key: 'api_key',
        required: true,
        label: {
          'en': 'API Key',
          'zh-Hans': 'API Key',
        },
        placeholder: {
          'en': 'Enter your API KEY',
          'zh-Hans': '在此输入您的 API KEY',
        },
      },
    ],
  },
}

export default config
