import styles from "./footer-top.module.css";
export const FooterTop = () => {
  return (
    <div className={styles.footer_top_container}>
    <div className={styles.footer_ul_container}>
      <ul>
        <li>
          <span>ИНФОРМАЦИЯ</span>
        </li>
        <li><p>Златоустовские ножи в Москве и Московской области</p></li>
        <li><p>Ножевые стали</p></li>
        <li><p>О нас</p></li>
        <li><p>Условия оплаты и доставки</p></li>
        <li><p>Политика конфиденциальности</p></li>
      </ul>
    </div>
    <div className={styles.footer_ul_container}>
      <ul>
        <li><span>СЛУЖБА ПОДДЕРЖКИ</span></li>
        <li><p>Контактная информация</p></li>
        <li><p>Возврат товара</p></li>
        <li><p>Карта сайта</p></li>
      </ul>
    </div>
    <div className={styles.footer_ul_container}>
      <ul>
        <li><span>ДОПОЛНИТЕЛЬНО</span></li>
        <li><p>Подарочные сертификаты</p></li>
        <li><p>Партнеры</p></li>
        <li><p>Товары со скидкой</p></li>
      </ul>
    </div>
    <div className={styles.footer_ul_container}>
      <ul>
        <li><span>ЛИЧНЫЙ КАБИНЕТ</span></li>
        <li><p>Личный кабинет</p></li>
        <li><p>История заказов</p></li>
        <li><p>Мои закладки</p></li>
        <li><p>Рассылка новостей</p></li>
      </ul>
    </div>
  </div>
  
    
  );
};
