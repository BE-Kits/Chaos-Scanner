/** 爬虫参数 */

export interface CrawlerOption {
  // 爬取深度，如果设置为 1 就是单页面爬虫
  depth: number;

  // 单页面爬取出的最多的子节点数
  maxChildren: number;

  // 总站点的总延时
  timeout: number;

  // 单页面的延时
  pageTimeout: number;

  // 是否仅爬取同站内容
  isSameOrigin: boolean;

  // 是否忽略媒体资源
  isIgnoreAssets: boolean;

  // 是否设置为移动模式
  isMobile: boolean;

  // 是否开启缓存
  isDatastoreCache: boolean;

  // 页面 Cookie
  cookie: string;

  // 页面的 localStorage
  localStorage: object;
}

export const defaultCrawlerOption = {
  depth: 1,
  maxChildren: 20,
  timeout: 5 * 60 * 1000,
  pageTimeout: 30 * 1000,

  isSameOrigin: true,
  isIgnoreAssets: true,
  isMobile: false,
  isDatastoreCache: false,

  cookie: '',
  localStorage: {}
};

export default defaultCrawlerOption;
