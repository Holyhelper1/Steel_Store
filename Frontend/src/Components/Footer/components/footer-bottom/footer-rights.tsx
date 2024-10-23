import styles from "./footer-rights.module.css"
export const FooterRights = () => {
  return (

    <div className={styles.footer_rights_container}>
        <div>
          <p>
            Все материалы, размещенные на сайте, носят справочный характер и не
            являются{" "}
          </p>
          <p>
            публичной офертой, определяемойположениями Статьи 437 Гражданского
            кодекса Российской Федерации.{" "}
          </p>
          <p>
            При копировании материалов гиперссылка на www.zlatmax.ru
            обязательна!{" "}
          </p>
        </div>

        <div>
          <p>Златоустовские ножи www.zlatmax.ru ©</p>
        </div>
      </div>
  )
}