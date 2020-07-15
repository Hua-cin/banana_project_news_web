import sys
import datetime
from Banana_news_module import chinatimes_list_crawler
from Banana_news_module import ltn_list_crawler
from Banana_news_module import ltn_list_crawler_for_tag
from Banana_news_module import news_object
from Banana_news_module import content_crawler

if __name__ == '__main__':

    now = datetime.datetime.now()
    print("\n{}, {}".format(now, "01.program start."))

    try:
        pass
        # update chinatimes news-------------------------------------------------------------------------------------------
        # return article list and judge need update or not result
        chinatimes_article_list, chinatimes_need_update = chinatimes_list_crawler.chinatimes_list()
        # print(chinatimes_article_list)

        # if need, update chinatimes
        if chinatimes_need_update:
            for i in range(len(chinatimes_article_list)):
                reg_news = news_object.News()
                reg_news.allocation('中國時報', chinatimes_article_list[len(chinatimes_article_list)-1-i])
                reg_news.related, content_exist = reg_news.related_or_not(content_crawler.chinatimes_content)
                if content_exist:
                    reg_news.upload_to_db()

            now = datetime.datetime.now()
            print("{}, {}".format(now, "02.chinatimes update finish."))
        else:
            now = datetime.datetime.now()
            print("{}, {}".format(now, "03.chinatimes no need update."))

        # # # update ltn news-------------------------------------------------------------------------------------------------
        # ltn_for_tag = False
        #
        # # return article list and judge need update or not result
        # # choice which type webpage for ltn web
        # if ltn_for_tag: # for have tag web
        #     ltn_article_list, ltn_need_update = ltn_list_crawler_for_tag.ltn_list()
        # else:
        #     ltn_article_list, ltn_need_update = ltn_list_crawler.ltn_list()
        #
        # # if need, update ltn
        # if ltn_need_update:
        #     for i in range(len(ltn_article_list)):
        #         reg_news = news_object.News()
        #         reg_news.allocation('自由時報', ltn_article_list[len(ltn_article_list)-1-i])
        #         reg_news.related, content_exist = reg_news.related_or_not(content_crawler.ltn_content)
        #         if content_exist:
        #             reg_news.upload_to_db()
        #
        #     now = datetime.datetime.now()
        #     print("{}, {}".format(now, "04.ltn update finish."))
        # else:
        #     now = datetime.datetime.now()
        #     print("{}, {}".format(now, "05.ltn no need update."))


    except Exception as err:
        now = datetime.datetime.now()
        print("{}, {}, {}".format(now, "06.prgoram abnormal. STOP!", err))
        sys.exit(0)


