import smtplib
import os
import imghdr
from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('fercaswilia@gmail.com')
# EMAIL_PASSWORD = os.environ.get('Kofan6184')


# e = pd.read_excel("Email.xlsx")
# emails = e['Emails'].values

msg = EmailMessage()
msg['Subject'] = 'Hey Your Order Is Ready To Activated!'
msg['From'] = 'fercaswilia@gmail.com'

# for email in emails:
msg['To'] = 'sarwarjah@gmail.com,akashchakraborty606@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
  <meta name="GENERATOR" content="MSHTML 11.00.10570.1001">

  <title></title>
</head>

<body>
  <div class="adn ads" style="padding: 0px; color: rgb(34, 34, 34); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: medium; font-style: normal; font-weight: 400; word-spacing: 0px; border-left-color: currentColor; border-left-width: medium; border-left-style: none; display: flex; white-space: normal; orphans: 2; widows: 2; background-color: rgb(255, 255, 255); font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;" data-message-id="#msg-a:r878871275490687603" data-legacy-message-id="178884e19f3b741e">
    <div class="gs" style="margin: 0px; padding: 0px 0px 20px; width: 1631.47px;">
      <div>
        <div class="ii gt" id=":2k" style="margin: 8px 0px 0px; padding: 0px; font-size: 0.87rem; position: relative; direction: ltr;">
          <div class="a3s aiL" id=":2j" style="line-height: 1.5; overflow: hidden; font-family: Arial, Helvetica, sans-serif; font-size: small; font-style: normal; font-variant: normal; font-size-adjust: none; font-stretch: normal;">
            <table width="640" align="center" style="font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;" cellspacing="0" cellpadding="0">
              <tr>
                <td width="100%" align="center" style='padding: 8px 14px 10px 24px; color: rgb(51, 51, 51); font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif;'>DO NOT REPLY TO THIS MESSAGE. If you require Customer Service or Technical Support, please&nbsp;contact&nbsp;<strong>+1 (000)&nbsp;000 -0000</strong></td>
              </tr>
            </table>

            <table width="640" align="center" style="border: 1px solid rgb(181, 181, 181); border-image: none; font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: small;" cellspacing="0" cellpadding="0">
              <tr>
                <td style="padding-right: 24px; padding-left: 24px;">
                  <table width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style="padding-top: 16px; padding-bottom: 16px;">
                        <table align="left" cellspacing="0" cellpadding="0">
                          <tr>
                            <td><a href="http://www.norton.com/" target="_blank"><img width="131" height="50" class="gmail-CToWUd" style="display: block;" alt="Norton by Symantec" src="https://ci6.googleusercontent.com/proxy/2C7A-VqMJVf-ZxNbup-MLhfe_ZIfK21MfRUrqtpxxTzETdJGXzmm9npkLBuEDIk1tdcVuP_W4Kua9MhGkN1PkWO3hgQIeTfIFAmzrVHaHkUvPp6H-7u2azJzy5Muv7v6Pv3TNXLkJ6lHHkSvbITOwzFiyCkw5ZEXMh0d81-IbA=s0-d-e1-ft#http://buy-static.norton.com//estore/images/Non-Product/ARemail_images/Opt-out_emails/logo_norton_131x50.gif" border="0"></a></td>
                          </tr>
                        </table>

                        <table align="right" cellspacing="0" cellpadding="0">
                          <tr>
                            <td height="50" align="right" style='color: rgb(128, 128, 128); font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 12px; font-weight: bold;'>SERVICE NOTIFICATION</td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>

            <table width="640" align="center" style="font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: small; border-right-color: rgb(181, 181, 181); border-bottom-color: rgb(181, 181, 181); border-left-color: rgb(181, 181, 181); border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-right-style: solid; border-bottom-style: solid; border-left-style: solid;" cellspacing="0" cellpadding="0">
              <tr>
                <td style="padding: 32px 24px 24px;">
                  <table width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style='color: rgb(1, 1, 1); padding-bottom: 7px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 30px;'>Attention:</td>
                    </tr>

                    <tr>
                      <td style='color: rgb(1, 1, 1); padding-bottom: 16px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 20px;'>Your&nbsp;<span class="gmail-il">Norton</span>&nbsp;Subscription Is Renewed.<br>
                      <br>
                      <font color="#FF8000">Hello %NAME%</font></td>
                    </tr>

                    <tr>
                      <td style='color: rgb(1, 1, 1); padding-bottom: 16px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 14px;'>It’s great to have you as a member of Norton, Hope&nbsp; you enjoyed our services.<br>
                      We have processed your&nbsp;<span class="gmail-il">Norton</span>&nbsp;Auto-Renewal For Upcoming 1 Year Premium Plan</td>
                    </tr>
                  </table>

                  <table width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style='color: rgb(1, 1, 1); padding-bottom: 16px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 14px;'></td>
                    </tr>
                  </table>

                  <table width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style="padding-bottom: 16px;"></td>
                    </tr>
                  </table>

                  <table width="100%" bgcolor="#F2F2F2" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style="padding: 16px;">
                        <table cellspacing="0" cellpadding="0">
                          <tr>
                            <td style='color: rgb(1, 1, 1); padding-bottom: 10px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 14px;'><b>Order No : NTN5425869871265<br>
                            <br>
                            You’ve Automatic Renewal on the following:</b></td>
                          </tr>

                          <tr>
                            <td style='color: rgb(1, 1, 1); padding-bottom: 10px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 14px;'>Your Product:&nbsp;<span class="gmail-il">Norton</span>™ Internet Security</td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>

                  <table width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style='color: rgb(1, 1, 1); padding-top: 16px; padding-bottom: 8px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 14px;'><br></td>
                    </tr>

                    <tr>
                      <td style='color: rgb(1, 1, 1); font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 14px;'>
                        <table cellspacing="0" cellpadding="0">
                          <tr>
                            <td style='padding-right: 16px; padding-bottom: 10px; padding-left: 16px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif;'>
                              <table width="400" style="color: rgb(34, 34, 34); font-family: arial; font-size: 11px;" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                  <td width="240" style="padding: 3px 0px 3px 15px; font-family: Arial, sans-serif; border-bottom-color: rgb(211, 211, 211); border-bottom-width: 1px; border-bottom-style: solid; background-color: rgb(243, 243, 243);"><font size="4">Product Name</font></td>

                                  <td width="50" align="center" style="padding: 3px 0px; font-family: Arial, sans-serif; border-bottom-color: rgb(211, 211, 211); border-bottom-width: 1px; border-bottom-style: solid; background-color: rgb(239, 245, 246);"><font size="4">Quantity</font></td>

                                  <td width="110" align="right" style="padding: 3px 15px 3px 0px; font-family: Arial, sans-serif; border-bottom-color: rgb(211, 211, 211); border-bottom-width: 1px; border-bottom-style: solid; background-color: rgb(239, 245, 246);"><font size="4">Amount</font></td>
                                </tr>

                                <tr>
                                  <td style="padding: 5px 0px 5px 15px; font-family: Arial, sans-serif; border-bottom-color: rgb(211, 211, 211); border-bottom-width: 1px; border-bottom-style: solid;"><font size="4">Norton Internet Security - Renewal</font></td>

                                  <td align="center" style="padding: 5px 0px; font-family: Arial, sans-serif; border-bottom-color: rgb(211, 211, 211); border-bottom-width: 1px; border-bottom-style: solid;"><font size="4">1</font></td>

                                  <td align="right" style="padding: 5px 15px 5px 0px; font-family: Arial, sans-serif; border-bottom-color: rgb(211, 211, 211); border-bottom-width: 1px; border-bottom-style: solid;"><font size="4">$ 321.56</font></td>
                                </tr>
                              </table><font size="4" style="color: rgb(34, 34, 34); font-family: arial;"><br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<wbr>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Tax :&nbsp;&nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$0.00&nbsp;&nbsp;&nbsp;<br>
                              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<wbr>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Total Paid : $ 285.08 USD</strong></font>
                              <hr id="gmail-false">
                            </td>
                          </tr>

                          <tr>
                            <td style='padding-right: 16px; padding-bottom: 10px; padding-left: 16px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif;'><br></td>
                          </tr>

                          <tr>
                            <td style='padding-right: 16px; padding-bottom: 10px; padding-left: 16px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif;'><br></td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>

                  <table width="100%" cellspacing="0" cellpadding="0">
                    <tr>
                      <td style='color: rgb(1, 1, 1); padding-top: 24px; font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 24px;'>Thank you.</td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>

            <table width="640" align="center" style="font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: small; border-right-color: rgb(181, 181, 181); border-bottom-color: rgb(181, 181, 181); border-left-color: rgb(181, 181, 181); border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-right-style: solid; border-bottom-style: solid; border-left-style: solid;" cellspacing="0" cellpadding="0">
              <tr>
                <td style="padding: 5px 24px;">
                  <table align="left" cellspacing="0" cellpadding="0">
                    <tr>
                      <td height="38" style='color: rgb(1, 1, 1); font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 11px;'>
                        <ul>
                          <li><font face="Geneva, Arial, Helvetica, sans-serif" size="3">Please contact Technical Support at&nbsp;<strong><font face="Segoe UI">+1 (000)&nbsp;000-0000</font></strong> For any Question</font></li>
                        </ul>
                      </td>
                    </tr>
                  </table>

                  <table align="right" cellspacing="0" cellpadding="0">
                    <tr>
                      <td>
                        <table cellspacing="0" cellpadding="0">
                          <tr>
                            <td style="padding-top: 8px; padding-right: 5px; padding-left: 5px;"><a href="https://www.facebook.com/Norton" target="_blank"><br></a></td>

                            <td style="padding-top: 8px; padding-right: 5px; padding-left: 5px;"><a href="https://twitter.com/nortononline" target="_blank"><br></a></td>

                            <td style="padding-top: 8px; padding-right: 5px; padding-left: 5px;"><a href="https://www.youtube.com/user/norton" target="_blank"><br></a></td>

                            <td style="padding-top: 8px; padding-right: 5px; padding-left: 5px;"><a href="https://plus.google.com/+Norton/posts" target="_blank"><br></a></td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>

            <table width="640" align="center" style="font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: small; border-right-color: rgb(181, 181, 181); border-bottom-color: rgb(181, 181, 181); border-left-color: rgb(181, 181, 181); border-right-width: 1px; border-bottom-width: 1px; border-left-width: 1px; border-right-style: solid; border-bottom-style: solid; border-left-style: solid;" cellspacing="0" cellpadding="0">
              <tr>
                <td style='padding: 16px 24px 32px; color: rgb(51, 51, 51); font-family: "Helvetica Neue", "Segoe UI", "Lucida Grande", "Lucida Sans", Lucida, Arial, sans-serif; font-size: 10px;'>Symantec Corporation, 350 Ellis St., Mountain View, California 94043, USA<br>
                FEIN: 77-0181864, Canadian GST #: 12801 3208 RT0001; QST # 1211858032<br>
                Canadian Customers: Shipping charges do not include any Brokerage Fees, Customs Fees or Taxes that you may be charged.<br>
                <br>
                <strong>Tax Disclosure:</strong><br>
                <br>
                Symantec Corporation, 350 Ellis St., Mountain View, California 94043, USA<br>
                FEIN: 77-0181864, Canadian GST #: 12801 3208 RT0001; QST # 1211858032<br>
                Canadian Customers: Shipping charges do not include any Brokerage Fees, Customs Fees or Taxes that you may be charged.<br>
                <br>
                <br>
                Total price shown is inclusive of VAT at an applicable rate for the identified customer country.<br>
                <br>
                <strong>EU resident customers</strong>&nbsp;(Seller's VAT No.&nbsp;<strong>IE6557355A</strong>):<br>
                Total price shown includes VAT at the standard rate applicable in the customer country.<br>
                Non-Irish business customers who provide VAT numbers will be charged a price exclusive of VAT - customers must self-account for VAT in accordance with art.196 of EU Directive.<br>
                <strong>Swiss resident customers</strong>&nbsp;(Seller's VAT No.&nbsp;<strong>CHE-113.760.836MWST</strong>):<br>
                Total price shown includes Swiss VAT at the standard rate.<br>
                <strong>Norwegian resident customers</strong>&nbsp;(Seller's VAT No.&nbsp;<strong>2017164</strong>):<br>
                Total price shown includes Norwegian VAT at the standard rate.<br>
                Business customers who provide VAT numbers will be charged price exclusive of VAT - customers must self-account for VAT in Norway.<br>
                <strong>Other customers</strong>&nbsp;(Seller's VAT No.&nbsp;<strong>IE6557355A</strong>):<br>
                Total price charged is VAT exclusive. <font face="Arial, Helvetica, sans-serif" size="2">Customers</font> are advised to follow local taxation rules.<br>
                <br>
                Symantec Asia Pacific Pte Ltd, 6, Temasek Blvd, Suntec Tower 4, #11-01, Singapore 038986<br>
                Tax invoice GST registration number: 200304231M<br>
                Goods and Services Tax ("GST") at 7% applies to the supplies of goods and services made in Singapore. The GST is also applicable to the imports of goods.<br>
                <br>
                Copyright © 2015 Symantec Corporation. All rights reserved. Symantec, the Symantec Logo, the Checkmark Logo,&nbsp;<span class="gmail-il">Norton</span>&nbsp;and&nbsp;<span class="gmail-il">Norton</span>&nbsp;by Symantec are trademarks or registered trademarks of Symantec Corporation or its affiliates in the U.S. and other countries. Other names may be trademarks of their respective owners.<br>
                <br></td>
              </tr>
            </table>
          </div>
        </div>

        <div class="hi" style="background: rgb(242, 242, 242); margin: 0px; padding: 0px; width: auto; border-bottom-right-radius: 1px; border-bottom-left-radius: 1px;"></div>
      </div>
    </div>

    <div class="ajx" style="clear: both;"></div>
  </div>

  <div class="gA gt acV" style="background: rgb(255, 255, 255); margin: 0px; padding: 0px; width: auto; color: rgb(34, 34, 34); text-transform: none; text-indent: 0px; letter-spacing: normal; font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; font-size: 0.87rem; font-style: normal; font-weight: 400; word-spacing: 0px; border-top-color: currentColor; border-top-width: medium; border-top-style: none; white-space: normal; orphans: 2; widows: 2; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px; font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text-decoration-thickness: initial; text-decoration-style: initial; text-decoration-color: initial;">
    <div class="gB xu" style="padding: 0px; border-top-color: currentColor; border-top-width: 0px; border-top-style: none;">
      <div class="ip iq" style="margin: 0px; padding: 16px 0px; clear: both; border-top-color: currentColor; border-top-width: medium; border-top-style: none;">
        <div id=":2l">
          <table class="cf wS" role="presentation" style="border-collapse: collapse;">
            <tr>
              <td class="amq" style="margin: 0px; padding: 0px 16px; width: 44px; font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif; vertical-align: top; visibility: hidden;"></td>

              <td class="amr" style="margin: 0px; padding: 0px; width: 1630.93px; font-family: Roboto, RobotoDraft, Helvetica, Arial, sans-serif;">
                <div class="nr wR" style="margin: 0px !important; padding: 0px; border-radius: 1px; border: currentColor !important; transition:none; border-image: none !important; color: rgb(34, 34, 34); box-sizing: border-box; background-color: rgb(255, 255, 255);">
                  <br>
                </div>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
""", subtype='html')


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('fercaswilia@gmail.com','Kofan6184')
server.send_message(msg)
server.quit()

