from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from .models import Video



def video_list(request):
	video_list = Video.objects.all()
	return render(request, 'video/video_list.html',{'video_list': video_list})

def video_detail(request,video_id):
	video = Video.objects.get(id=video_id)
	if(request.method=="POST"):
		title = request.POST.get('title','')
		key = request.POST.get('key','')

		video.title = title
		video.key = key
		video.save()
		redirect('video/'+str(video.id))

	return render(request,'video/video_detail.html',{'video':video})

def video_new(request):
	if(request.method == 'POST'):
		# title = request.POST['title']
		# video_key= request.POST['video_key']
		title = request.POST.get('title','')
		key = request.POST.get('key','')  #없으면 ''를 보내겠다. 위 주석처럼 하는 경우 빈게 오면 에러를 뿜음

		video = Video(
			title=title,
			key=key,
		)
		video.save()
		return redirect('/video/' +str(video.id))

		# return redirect(reverse('video:detail',video.id))
		#reverse라는 애는 urls.py에서 video안에 :로 name을 찾는 과정을 해석해줌
		#즉 video_detail/video.id

	# elif (request.method == 'GET'):
	return render(request,'video/video_new.html')
	#그냥 url을 치고 들어오면 get 메소드로 들어오게 됨

def video_delete(request,video_id):
	Video.objects.get(id=video_id).delete()
	return redirect('/video/')
