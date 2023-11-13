css = '''
<style>
.chat-message {
    padding: 1,5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex;
}
.chat-message.bot{
    background-color: #475063;
}
.chat-message.user{
    background-color: #463f3a;
}
.chat-message .avatar{
    width: 15%;
}
.chat-message .avatar img{
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message{
    width: 85%;
    padding: 0 1.5rem;
    color:#fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://m.media-amazon.com/images/I/51DBd7O6GEL.jpg" alt="" style="" />
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/D4E03AQF-CVGAGZ6TDw/profile-displayphoto-shrink_800_800/0/1699718040792?e=1704931200&v=beta&t=bHfqWysCn-Ei0DiNUbwg9mo0QlHqj7FsVsFaStqhG3A" alt="" />
    </div>
    <div class="message">{{MSG}}</div>
</div>

'''
